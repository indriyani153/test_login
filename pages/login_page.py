from selenium.webdriver.common.by import By
from locators.login_locator import LoginLocator

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_label_login(self):
        self.driver.find_element(By.CSS_SELECTOR, LoginLocator.label_login).click()

    def input_username(self, username):
        self.driver.find_element(By.ID, LoginLocator.username).send_keys(username)
    
    def input_pass(self, password):
        self.driver.find_element(By.ID, LoginLocator.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, LoginLocator.button_login).click()
    
    def failed_login(self):
       show = self.driver.find_element(By.ID, LoginLocator.failed_login).text
       return show
    
    def failed_login_invalid(self):
        show = self.driver.find_element(By.CSS_SELECTOR, LoginLocator.failed_login_invalid).text
        return show
    
    def success_login(self):
        show = self.driver.find_element(By.CSS_SELECTOR, LoginLocator.success_login).text
        return show
