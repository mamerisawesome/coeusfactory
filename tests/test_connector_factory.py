def test_no_interface():
    from coeusfactory import ConnectorFactory
    connector = ConnectorFactory()
    assert connector.db == None

def test_nonexistent_interface():
    from coeusfactory import ConnectorFactory
    connector = ConnectorFactory("not_a_db")
    assert connector.db == None


def test_mongo_connector():
    from coeusfactory import ConnectorFactory
    connector = ConnectorFactory(
        "mongo",
        db="test",
        collection="test-collection",
    )

    try:
        assert connector.db.initialize() != False
    except Exception:
        assert False
