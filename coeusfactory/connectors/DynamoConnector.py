from .BaseConnector import BaseConnector


class DynamoConnector(BaseConnector):
    config_params = [
        "region"
    ]

    def __init__(self, event=None, **kwargs):
        self.config = self._handle_init_kwargs(kwargs)
        self.event = event
        base = super(DynamoConnector, self)
        base.__init__(__name__)

    def initialize(self):
        import boto3
        config = self.config

        self._validate_config(config)
        self.client = boto3.client(
            "dynamodb",
            region_name=config["region"])

        self.event.sendMessage("initialized")

    def connect(self):
        from pymongo.database import Database
        config = self.config
        self.db = Database(self.client, config["db"])

        # flush all params
        self.config = None

        self.event.sendMessage("connected")

    def disconnect(self):
        self.client = None
        self.event.sendMessage("disconnected")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, table_name):
        import boto3

        dynamo = boto3.resource("dynamodb", region_name=self.region)
        if self.table_name not in self.client.list_tables()["TableNames"]:
            table = dynamo.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {
                        "AttributeName": "sender_id",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "session_date",
                        "KeyType": "RANGE"
                    },
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "sender_id",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "session_date",
                        "AttributeType": "N"
                    },
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 5
                },
            )

            # use waiter to watch for table existence
            waiter = table.meta.client.get_waiter("table_exists")
            waiter.wait(TableName=table_name)

        self._model = dynamo.Table(table_name)
