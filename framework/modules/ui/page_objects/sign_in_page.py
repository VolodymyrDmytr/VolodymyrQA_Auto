from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL_Git = 'https://github.com/login'
    URL_Facebook = 'https://facebook.com/login'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL_Git)

    def go_to_f(self):
        self.driver.get(SignInPage.URL_Facebook)

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def loggin(self, username, password):
        log_elem = self.driver.find_element(By.ID, 'login_field')
        log_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, 'password')
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, 'commit')
        btn_elem.click()

    def go_to_first_reposetory_after_loggin(self):
        repo = self.driver.find_element(By.XPATH, '//form[@id="dashboard-repositories-box"]/div/div/div/ul/li[1]/div/div/a')
        repo.click()

    def loggin_Facebook(self, username, password):
        log_elem = self.driver.find_element(By.ID, 'email')
        log_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, 'pass')
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, 'login')
        btn_elem.click()
