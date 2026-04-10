from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class PimPage():

    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")

    def add_employee(self, first, last):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

        
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first)


        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
        


