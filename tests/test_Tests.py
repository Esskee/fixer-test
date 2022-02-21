import pytest
from app.app import api_call, convert_curr
from config import basevars


def test_api():
    d = api_call(basevars.url, basevars.key, '', '')
    for key, val in d.items():
        assert val
