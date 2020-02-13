from rainbow import RainbowLogger
from pymongo import DESCENDING
from .BaseRepository import BaseRepository
logger = RainbowLogger(__name__)


class MongoRepository(BaseRepository):
    def __init__(self, model, database=None, name=__name__):
        base = super(MongoRepository, self)
        base.__init__(
            model=model,
            database=database,
            name=name
        )

    def get_all(self):
        return [c for c in self.model.find(sort=[('_id', DESCENDING)])]

    def get_by_id(self, id):
        return self.model.find_one({"_id": id}, sort=[('_id', DESCENDING)])

    def get(self, query):
        return self.model.find_one(query, sort=[('_id', DESCENDING)])

    def add(self, value):
        return self.model.insert_one(value)

    def delete_by_id(self, id):
        return self.model.find_one_and_delete(
            {"_id": id},
            sort=[('_id', DESCENDING)]
        )

    def delete(self, query):
        return self.model.find_one_and_delete(
            query,
            sort=[('_id', DESCENDING)]
        )

    def update_by_id(self, id, value):
        return self.model.find_one_and_update(
            {"_id": id},
            {"$set": value},
            sort=[('_id', DESCENDING)]
        )

    def update(self, query, value):
        return self.model.find_one_and_update(
            query,
            {"$set": value},
            sort=[('_id', DESCENDING)]
        )

    def count(self, query={}):
        return self.model.count_documents(query)
