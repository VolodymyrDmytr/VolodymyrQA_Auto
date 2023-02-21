from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def loggin(self, username, password):
        log_elem = self.driver.find_element(By.ID, 'login_field')
        log_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, 'password')
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, 'commit')
        btn_elem.click()
