import logging
from pymongo import DESCENDING
from .BaseRepository import BaseRepository
logger = logging.getLogger(__name__)


class MongoRepository(BaseRepository):
    def __init__(self, model, database=None, name=__name__):
        base = super(MongoRepository, self)
        base.__init__(
            model=model,
            database=database,
            name=name
        )

    def get_all(self, targets=[]):
        query_targets = self._get_targets(targets)
        cursor = self.model.find(
            {},
            query_targets,
            sort=[("_id", DESCENDING)]
        )

        return [c for c in cursor]

    def get_by_id(self, id):
        return self.get({"_id": id})

    def get(self, query, targets=[]):
        query_targets = self._get_targets(targets)
        return self.model.find_one(
            query,
            query_targets,
            sort=[("_id", DESCENDING)]
        )

    def add(self, value):
        return self.model.insert_one(value)

    def delete_by_id(self, id):
        return self.delete({"_id": id})

    def delete(self, query):
        return self.model.find_one_and_delete(
            query,
            sort=[("_id", DESCENDING)]
        )

    def update_by_id(self, id, value, **kwargs):
        return self.update({"_id": id}, value, **kwargs)

    def update(self, query, value, mode="set", upsert=False, date_key=None):
        from pymongo.collection import ReturnDocument

        mode = "${}".format(mode)
        update_operations = {
            mode: value
        }

        if date_key:
            update_operations["$currentDate"] = {
                date_key: True
            }

        return self.model.find_one_and_update(
            query,
            update_operations,
            sort=[("_id", DESCENDING)],
            upsert=upsert,
            return_document=ReturnDocument.AFTER
        )

    def count(self, query={}):
        return self.model.count_documents(query)

    def _get_targets(self, targets=None):
        if not targets:
            return None

        query_targets = {}
        for k in targets:
            query_targets[k] = 1
        return query_targets
