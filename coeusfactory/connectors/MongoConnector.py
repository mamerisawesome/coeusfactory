from .BaseConnector import BaseConnector
from rainbow import RainbowLogger
logger = RainbowLogger(__name__)


class MongoConnector(BaseConnector):
    config_params = [
        "host",
        "username",
        "password",
        "auth_source",
        "db",
        "collection",
        "connect",
    ]

    def __init__(self, event=None, **kwargs):
        self.config = self._handle_init_kwargs(kwargs)
        self.event = event
        base = super(MongoConnector, self)
        base.__init__(__name__)

    def initialize(self):
        from pymongo import MongoClient
        config = self.config

        self._validate_config(config)

        if "auth_source" in config and not config["auth_source"]:
            config["auth_source"] = "admin"

        if "connect" in config and not config["connect"]:
            config["connect"] = False

        self.client = MongoClient(
            config["host"],
            username=config["username"],
            password=config["password"],
            authSource=config["auth_source"],
            connect=config["connect"],
        )

        # flush sensitive configurations after creating connection
        flush_params = (
            "host",
            "username",
            "password",
            "auth_source",
            "connect"
        )

        for param in flush_params:
            self.config[param] = None

        self.event.sendMessage("initialized")

    def connect(self):
        from pymongo.database import Database
        config = self.config
        self.db = Database(self.client, config["db"])

        # flush all params
        self.config = None

        self.event.sendMessage("connected")

    def disconnect(self):
        self.client.close()
        self.event.sendMessage("disconnected")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, collection_name):
        self._model = self.db[collection_name]
