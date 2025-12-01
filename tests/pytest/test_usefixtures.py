import pytest

@pytest.fixture()
def clear_books_database():
    print("[FIXTURE] Удалялем все данные из базы данных")

@pytest.fixture()
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")


@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:
    def test_read_from_library(self):
        ...

    def test_delete_from_library(self):
        ...