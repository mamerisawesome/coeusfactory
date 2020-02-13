def test_no_interface():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory()
    assert cf.handler == None

def test_nonexistent_interface():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory("not_a_db")
    assert cf.handler == None
