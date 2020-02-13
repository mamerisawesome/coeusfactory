def test_base_connector():
    from coeusfactory.connectors.BaseConnector import BaseConnector

    try:
        bc = BaseConnector(__name__, test=None)
    except (EnvironmentError, OSError):
        assert True

    bc = BaseConnector(__name__)
    # return fails if no interface is created
    assert not bc.initialize()
    assert not bc.connect()
    assert not bc.disconnect()
