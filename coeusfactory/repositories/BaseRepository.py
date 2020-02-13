from rainbow import RainbowLogger
logger = RainbowLogger(__name__)


class BaseRepository():
    def __init__(self, model, to_entity=None, to_database=None, name=__name__):
        self.model = model
        self.to_entity = to_entity
        self.to_database = to_database
        logger.info("{} successfully initialized.".format(name))

    def get_all(self):
        return

    def get_by_id(self):
        return

    def add(self):
        return

    def remove(self):
        return

    def update(self):
        return

    def count(self):
        return
