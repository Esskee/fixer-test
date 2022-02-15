import pytest
from app.app import api_call, convert_curr
from config import basevars


def test_api():
    assert api_call(basevars.url, basevars.key, '', '') == '{"success":true}'


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1
