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

    def count(self):
        return False
