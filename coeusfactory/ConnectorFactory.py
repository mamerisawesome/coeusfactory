import logging
logger = logging.getLogger(__name__)


class ConnectorFactory():
    def __init__(self, interface=None, raw_name=False, **kwargs):
        if not interface:
            logger.warning("No database interface selected")
            self.handler = None
            return None

        from pubsub import pub
        self.event = pub
        self.interface = interface
        self.raw_name = raw_name
        self.handler = self._set_connector(**kwargs)
        self._set_events(['initialized', 'connected', 'disconnected'])

    def initialized(self):
        logger.info("Database initialized")

    def connected(self):
        logger.info("Database connected")

    def disconnected(self):
        self.handler = None
        logger.info("Database disconnected")

    def get_model(self, model):
        interface = self.interface
        if not model or not model[0].isalpha():
            return None

        if self.raw_name:
            self.handler.model = model
        else:
            model_name = model[0].upper()
            if len(model) > 1:
                model_name = model_name + model[1:].lower()
            self.handler.model = model_name

        module_prefix = interface[0].upper() + interface.lower()[1:]
        connectors = __import__("coeusfactory.repositories")
        connectors = getattr(connectors, "repositories")
        module = getattr(connectors, "{}Repository".format(module_prefix))
        return module(model=self.handler.model, database=self.handler.db)

    def _set_events(self, events_array):
        for event in events_array:
            self.event.subscribe(getattr(self, event), event)

    def _set_connector(self, **kwargs):
        interface = self.interface
        try:
            module_prefix = interface[0].upper() + interface.lower()[1:]
            connectors = __import__("coeusfactory.connectors")
            connectors = getattr(connectors, "connectors")
            module = getattr(connectors, "{}Connector".format(module_prefix))
            return module(event=self.event, **kwargs)
        except (ImportError, AttributeError):
            logger.error("{}Connector not available".format(module_prefix))
            return None
