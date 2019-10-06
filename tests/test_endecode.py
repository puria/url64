import pytest

from url64 import url64


@pytest.mark.parametrize('value, expected', [
    ("cG9sbA", "poll"),
    ("TUE", "MA"),
    ("MA", "0")
])
def test_decode(value, expected):
    assert url64.decode(value) == expected


@pytest.mark.parametrize('value, expected', [
    ("poll", "cG9sbA"),
    ("MA", "TUE"),
    ("0", "MA")
])
def test_encode(value, expected):
    assert url64.encode(value) == expected
