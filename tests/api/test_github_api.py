import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


"""
tests for Get emoji
"""


# в цьому тесті я додала фікстуру щоб потренуватись
@pytest.mark.api
def test_check_emoji_in_list(github_api):
    r = github_api.search_emoji()
    assert "accordion" in r


# а в цьому не додавала адже для емоджі немає параметрів
@pytest.mark.api
def test_check_emoji_not_in_list():
    api = GitHub()
    r = api.search_emoji()
    assert "sddsq" not in r


"""
tests for Get List Commits
"""


@pytest.mark.api
def test_check_commits_list(github_api):
    r = github_api.search_commit("lgav11", "lena_repo1")
    assert r[0]["commit"]["author"]["name"] == "Olena Havryliuk"


@pytest.mark.api
def test_check_commits_list_invalid(github_api):
    r = github_api.search_commit(" ", " ")
    assert r["message"] == "Not Found"
