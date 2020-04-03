import logging
logger = logging.getLogger(__name__)


class BaseRepository(object):
    def __init__(self, model, database=None, name=__name__):
        self.model = model
        self.database = database
        logger.info("{} successfully initialized.".format(name))

    def get_all(self):
        return False

    def get_by_id(self, id):
        return False

    def get(self, query):
        return False

    def add(self, value):
        return False

    def delete_by_id(self, id):
        return False

    def delete(self, query):
        return False

    def update_by_id(self, id, value):
        return False

    def update(self, query, value):
        return False

    def count(self, query={}):
        return False
