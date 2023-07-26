import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == "Olena"


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == "Havryliuk"


@pytest.mark.check
def test_check_name(user):
    assert user.name == "Olena"


@pytest.mark.check
def test_check_second_name(user):
    assert user.second_name == "Havryliuk"
