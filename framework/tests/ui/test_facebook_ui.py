from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time


@pytest.mark.ui
def test_incorrect_data_to_sign_in():
    sign_in = SignInPage()
    sign_in.go_to_f()
    sign_in.loggin_Facebook("wrong@email.com", "wrongpassword")
    time.sleep(4)
    print(f"1 - {sign_in.driver.title}")
    assert sign_in.check_title("Log in to Facebook")  # налашування мови на Англ.


@pytest.mark.ui
def test_correct_data_to_sign_in():
    sign_in = SignInPage()
    sign_in.go_to_f()
    sign_in.loggin_Facebook("~~", "~~") # sensitive data
    time.sleep(4)
    print(f"2 - {sign_in.driver.title}")
    assert sign_in.check_title("Facebook")
