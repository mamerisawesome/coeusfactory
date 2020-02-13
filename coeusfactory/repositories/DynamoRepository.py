from rainbow import RainbowLogger
from .BaseRepository import BaseRepository
logger = RainbowLogger(__name__)


class DynamoRepository(BaseRepository):
    def __init__(self, model, database=None, name=__name__):
        base = super(DynamoRepository, self)
        base.__init__(
            model=model,
            database=database,
            name=name
        )

    def get_all(self):
        return False

    def get_by_id(self, id):
        return self.get({"id": id})

    def get(self, query):
        return self.model.get_item(Key=query)

    def add(self, value):
        return self.model.put_item(Item=value)

    def delete_by_id(self, id):
        return self.delete({"id": id})

    def delete(self, query):
        return self.model.delete_item(Key=query)

    def update_by_id(self, id, value: dict):
        return self.update({"id": id}, value)

    def update(self, query, value):
        update_expression = []
        update_values = {}
        for k in value.keys():
            update_expression += ["{0} :{0}".format(k)]
            update_values[":{}".format(k)] = value[k]

        return self.model.update_item(
            Key=query,
            UpdateExpression="SET " + ",".join(update_expression),
            ExpressionAttributeValues=update_values
        )

    def count(self):
        return self.model.item_count
