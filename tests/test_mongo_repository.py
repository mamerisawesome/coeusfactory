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

def test_mongo_update_return_updated_entry():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")
    user_id = Users.add({"name": "Newly added user"}).inserted_id

    res = Users.update({"name": "Newly added user"}, {"name": "Newly updated user"})
    assert res["name"] == "Newly updated user"

def test_mongo_update_handle_upsert():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()
    Users = cf.get_model("users")

    res = Users.update(
        {"name": "User does not exist"},
        {"name": "User will not save"},
    )

    assert res == None

    res = Users.update(
        {"name": "User does not exist"},
        {"name": "User should exist now"},
        upsert=True
    )

    assert res["name"] == "User should exist now"

def test_mongo_update_push_to_array():
    from coeusfactory import ConnectorFactory
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    Products = cf.get_model("products")
    products_id = Products.add({
        "product_list": {
            "actual_list": [
                "product 1",
                "product 2",
                "product 3"
            ]
        }
    }).inserted_id

    res = Products.update_by_id(
        products_id,
        {
            "product_list.actual_list": "product 4"
        },
        mode="push"
    )

    assert res["product_list"]["actual_list"] == [
        "product 1",
        "product 2",
        "product 3",
        "product 4",
    ]


def test_mongo_update_date_update():
    from coeusfactory import ConnectorFactory
    from datetime import datetime
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    Profiles = cf.get_model("profiles")
    profiles_id = Profiles.add({
        "username": "Cute ni Almer",
        "password": "super-secret",
        "date_created": datetime.now(),
        "date_updated": datetime.now()
    }).inserted_id

    old_res = Profiles.get({"username": "Cute ni Almer"})

    res = Profiles.update(
        {"username": "Cute ni Almer"},
        {
            "password": "pwede-bang-gamitin-account-mo"
        },
        date_key="date_updated"
    )

    new_time = (datetime.now() - res["date_updated"]).total_seconds()
    old_time = (datetime.now() - old_res["date_updated"]).total_seconds()

    assert new_time > old_time

def test_mongo_set_targets():
    from coeusfactory import ConnectorFactory
    from datetime import datetime
    cf = ConnectorFactory(
        "mongo",
        db="test",
    )

    cf.handler.initialize()
    cf.handler.connect()

    Conversations = cf.get_model("conversations")

    Conversations.add({
        "message": "Hello lord bolgadort",
        "reply": "It's levi-o-sa!",
        "date_created": datetime.now(),
        "date_updated": datetime.now()
    })

    Conversations.add({
        "message": "Com'on vamonos",
        "reply": "Dora did it",
        "date_created": datetime.now(),
        "date_updated": datetime.now()
    })

    Conversations.add({
        "message": "Can you feel the love tonight",
        "reply": "Toooonigghtttttt",
        "date_created": datetime.now(),
        "date_updated": datetime.now()
    })

    conversations = Conversations.get_all(targets=["reply"])

    sorted_expected = sorted(["It's levi-o-sa!", "Dora did it", "Toooonigghtttttt"])
    sorted_actual = sorted(list(set([c["reply"] for c in conversations])))
    assert sorted_expected == sorted_actual
