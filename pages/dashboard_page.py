from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

    profile_icon = (By.XPATH,  "//p[@class='oxd-userdropdown-name']") 
    logout_button = (By.XPATH,  "//a[normalize-space()='Logout']") 

    def logout(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.profile_icon)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()
          
        