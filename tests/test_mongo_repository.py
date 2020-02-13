def test_mongo_insert():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user = Users.add({"name": "Test User"})
    assert Users.get_by_id(user.inserted_id) != None
    assert Users.get_by_id(user.inserted_id)["name"] == "Test User"

def test_mongo_delete():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user = Users.add({"name": "Test User"})

    Users.delete_by_id(user.inserted_id)
    assert Users.get_by_id(user.inserted_id) == None

def test_mongo_update():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user = Users.add({"name": "Test User"})

    Users.update_by_id(user.inserted_id, {"name": "New Test Name"})
    assert Users.get_by_id(user.inserted_id)["name"] == "New Test Name"

def test_mongo_count():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    users = Users.get_all()
    assert len(users) == Users.count()

def test_mongo_get_by_query():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user_id = Users.add({"name": "Newly added user"}).inserted_id
    user = Users.get({"name": "Newly added user"})

    assert user_id == user["_id"]

def test_mongo_delete_by_query():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user_id = Users.add({"name": "Newly added user"}).inserted_id
    Users.delete({"name": "Newly added user"})

    assert Users.get_by_id(user_id) == None

def test_mongo_update_by_query():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user_id = Users.add({"name": "Newly added user"}).inserted_id
    Users.update({"name": "Newly added user"}, {"name": "Newly updated user"})

    assert Users.get_by_id(user_id)["name"] == "Newly updated user"
