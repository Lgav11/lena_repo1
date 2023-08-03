import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None
        self.owner = None
        self.repo = None

    def create(self):
        self.name = "Olena"
        self.second_name = "Havryliuk"

    def remove(self):
        self.name = ""
        self.second_name = ""

    def create_repo(self):
        self.owner = "lgav11"
        self.repo = "lena_repo1"


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


# фікстура для сворення owner,repo для Get Commit запиту
@pytest.fixture
def user_repo():
    repo1 = User()
    repo1.create_repo()

    yield repo1


@pytest.fixture
def db_create():
    db = Database()
    yield db
