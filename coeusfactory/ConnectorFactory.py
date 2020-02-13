from rainbow import RainbowLogger
logger = RainbowLogger(__name__)


class ConnectorFactory():
    def __init__(self, interface=None, **kwargs):
        if not interface:
            logger.warning("No database interface selected")
            self.db = None
            return None

        from pubsub import pub
        self.event = pub
        self.db = self._set_connector(interface, **kwargs)
        self._set_events(['initialized', 'connected', 'disconnected'])

    def _set_events(self, events_array):
        for event in events_array:
            self.event.subscribe(getattr(self, event), event)

    def _set_connector(self, interface, **kwargs):
        try:
            module_prefix = interface[0].upper() + interface.lower()[1:]
            connectors = __import__("coeusfactory.connectors")
            connectors = getattr(connectors, "connectors")
            module = getattr(connectors, "{}Connector".format(module_prefix))
            return module(event=self.event, **kwargs)
        except (ImportError, AttributeError):
            logger.error("Database interface not available")
            return None

    def initialized(self):
        logger.info("Database initialized")

    def connected(self):
        logger.info("Database connected")

    def disconnected(self):
        logger.info("Database disconnected")
