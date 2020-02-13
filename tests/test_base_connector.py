def test_base_connector():
    from coeusfactory.connectors.BaseConnector import BaseConnector

    try:
        connector = BaseConnector(__name__, test=None)
    except (EnvironmentError, OSError):
        assert True

    connector = BaseConnector(__name__)
    # return fails if no interface is created
    assert not connector.initialize()
    assert not connector.connect()
    assert not connector.disconnect()
