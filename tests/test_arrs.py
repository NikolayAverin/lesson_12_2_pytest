from utils import arrs
import pytest


@pytest.fixture()
def test_list():
    return [1, 2, 3]


def test_get(test_list):
    assert arrs.get(test_list, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(test_list):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(test_list, 1) == [2, 3]
    assert arrs.my_slice([], ) == []
    assert arrs.my_slice(test_list, ) == test_list
