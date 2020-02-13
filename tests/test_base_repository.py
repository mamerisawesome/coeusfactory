def test_base_repository():
    from coeusfactory.repositories.BaseRepository import BaseRepository

    br = BaseRepository(model="test", name=__name__)

    # return fails if no interface is created
    assert not br.get_all()
    assert not br.get_by_id(0)
    assert not br.get({})
    assert not br.add({})
    assert not br.delete_by_id(0)
    assert not br.delete({})
    assert not br.update_by_id(0, {})
    assert not br.update({}, {})
    assert not br.count()
