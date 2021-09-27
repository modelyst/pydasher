from pydantic import BaseModel
from pydasher.base import HashMixIn


class Dummy(HashMixIn, BaseModel):
    key_1: str
    key_2: str
    key_3: float
    _hashexclude_ = {"key_3"}


def test_basic_mixin():
    dummy = Dummy(key_1="1", key_2="2", key_3="3")
    assert isinstance(dummy, Dummy)
    assert dummy.dict() == {"key_1": "1", "key_2": "2", "key_3": 3.0}
    non_id_dict = dummy.to_dict()
    id_dict = dummy.to_dict(id_only=True)
    assert "key_3" in non_id_dict
    assert "key_3" not in id_dict
    assert dummy.hash == dummy.from_dict(dummy.to_dict()).hash


class NestedDummy(HashMixIn, BaseModel):
    key_1: str
    key_2: Dummy
    key_3: float
    _hashexclude_ = {"key_3"}


def test_nested_mixin():
    dummy = Dummy(key_1="1", key_2="2", key_3="3")
    nested_dummy = NestedDummy(key_1="1", key_2=dummy, key_3="3")
    assert nested_dummy.hash == nested_dummy.from_dict(nested_dummy.to_dict()).hash