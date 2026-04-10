from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")  
    login_button = (By.XPATH, "//button[@type='submit']") 

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_button)
        ).click()
        

    
        