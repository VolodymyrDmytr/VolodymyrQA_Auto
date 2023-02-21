import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = None
    assert user.name == None

@pytest.mark.check
def test_name(user):
    assert user.name == 'Volodymyr'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Dmytriiev'
