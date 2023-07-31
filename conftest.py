import pytest
from modules.api.clients.github import GitHub


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Olena"
        self.second_name = "Havryliuk"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()  # створюєм екземпляр класа юзер
    user.create()

    yield user  # повертає об’єкт після виклику методу об’єкту create в тести

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api
