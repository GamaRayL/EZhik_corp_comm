import pytest

from utils.database_manager import DatabaseManager


@pytest.fixture(scope='session')
def test_db(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp('test_db')
    db_path = temp_dir / 'test_db.db'

    test_base = DatabaseManager(str(db_path))
    yield test_base
    test_base.db.close()


def test_create_user(test_db):
    test_db.create_user('Ноунейм', 'Ноунеймов', '7777777')
    assert test_db.select_user('7777777') == (1, 'Ноунейм', 'Ноунеймов', '7777777')
