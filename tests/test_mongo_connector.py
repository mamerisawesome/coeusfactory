from hypothesis import given
from hypothesis import example
import hypothesis.strategies as st
from hypothesis.strategies import text

@given(param_name=text())
def test_string(param_name):
    assert type(param_name) == str

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

@given(collection_name=st.text())
@example(collection_name="")
@example(collection_name=".")
@example(collection_name="$")
def test_mongo_model(collection_name):
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    model = cf.get_model(collection_name)

    if cf.handler.model:
        model.add({"test_param": "Hello"})
        assert model.get({"test_param": "Hello"}) is not None

def test_mongo_model_switch_collection():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    model = cf.get_model("test_collection")
    model.add({"test_param": "Hello"})

    model = cf.get_model("test_collection_two")
    model.add({"test_param": "Hello"})
    assert model.get({"test_param": "Hello"}) is not None

def test_mongo_raw_model_name():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test"
    )

    cf.handler.initialize()
    cf.handler.connect()
    users = cf.get_model("users")

    assert "Users" in cf.handler.db.list_collection_names()

def test_mongo_raw_model_name():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
        raw_name=True
    )

    cf.handler.initialize()
    cf.handler.connect()
    users = cf.get_model("users")
    users.add({"data": True})

    assert "users" in cf.handler.db.list_collection_names()
