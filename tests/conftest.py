import pytest

@pytest.fixture(scope='session')
def db_conn():
    url = 'mongodb+srv://ESdataAdmin:Canyon321@cluster0.xmf8h.mongodb.net/smdata?authSource=admin&replicaSet=atlas-2b1n1h-shard-0'
    db = 'smdata'
    with db.connect(url) as conn:
        yield conn
