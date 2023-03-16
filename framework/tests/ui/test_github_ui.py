from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_incorrect_data_to_sign_in():
    sign_in = SignInPage()
    sign_in.go_to()
    sign_in.loggin("wrongemail@gmail.com", "wrongpassword")
    assert sign_in.check_title("Sign in to GitHub · GitHub")
    sign_in.driver.close()


@pytest.mark.ui
def test_correct_data_to_sign_in():
    sign_in = SignInPage()
    sign_in.go_to()
    sign_in.loggin("~~", "~~")  # sensitive data
    assert sign_in.check_title("GitHub")
    sign_in.driver.close()
