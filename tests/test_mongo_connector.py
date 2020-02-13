def test_mongo_cf():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    assert cf != None

def test_mongo_initialize():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    init_response = cf.handler.initialize()

    # should not return BaseConnector responses
    assert init_response != False

    # check Mongo Client if not none on init
    assert cf.handler.client != None

def test_mongo_connect():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    assert cf.handler.db != None

def test_mongo_disconnect():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    cf.handler.disconnect()
    assert cf.handler is None

def test_mongo_model():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    cf.handler.model = "test_collection"
    cf.handler.model.insert_one({"test_param": "Hello"})
    assert cf.handler.model.find_one({"test_param": "Hello"}) is not None

def test_mongo_model_switch_collection():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    cf.handler.model = "test_collection"
    cf.handler.model.insert_one({"test_param": "Hello"})

    cf.handler.model = "test_collection_two"
    cf.handler.model.insert_one({"test_param": "Hello"})
    assert cf.handler.model.find_one({"test_param": "Hello"}) is not None
