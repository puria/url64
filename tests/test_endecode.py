import pytest

import url64


@pytest.mark.parametrize('value, expected', [
    ("cG9sbA", "poll"),
    ("TUE", "MA"),
    ("MA", "0"),
    ("eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9", '{"alg": "HS256", "typ": "JWT"}')
])
def test_decode(value, expected):
    assert url64.decode(value) == expected


@pytest.mark.parametrize('value, expected', [
    ("<<???>>", "PDw_Pz8-Pg"),
    ("poll", "cG9sbA"),
    ("Hello world!", "SGVsbG8gd29ybGQh"),
    ("MA", "TUE"),
    ("0", "MA"),
    (dict(a=1, b="a", c=[1,"a"]), "eyJhIjogMSwgImIiOiAiYSIsICJjIjogWzEsICJhIl19"),
    (dict(alg="HS256", typ="JWT"), "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9")
])
def test_encode(value, expected):
    assert url64.encode(value) == expected
