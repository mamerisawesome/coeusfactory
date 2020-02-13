class BaseConnector(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.db = None
        self._model = None

        if "test" in kwargs:
            config = self._handle_init_kwargs(kwargs)
            self._validate_config(config, {})

    def initialize(self):
        return False

    def connect(self):
        return False

    def disconnect(self):
        return False

    def _handle_init_kwargs(self, kwargs):
        try:
            self.config_params
        except AttributeError:
            return {}

        config = {}
        for param in self.config_params:
            if param not in kwargs:
                config[param] = None
                continue

            config[param] = kwargs[param]

        return config

    def _validate_config(self, config, validation_check=True):
        # TODO validation_check conformed for the interface
        if validation_check:
            return True

        raise EnvironmentError("Config must conform with the interface")
