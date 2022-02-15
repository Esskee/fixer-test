import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope='session')
def db_conn():
    url = 'mongodb+srv://ESdataAdmin:Canyon321@cluster0.xmf8h.mongodb.net/smdata?authSource=admin&replicaSet=atlas-2b1n1h-shard-0'
    db = 'smdata'
    with db.connect(url) as conn:
        yield conn
