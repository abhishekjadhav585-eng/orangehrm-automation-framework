from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeListPage:

    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']") 
    employee_list = (By.XPATH, "//a[normalize-space()='Employee List']")
    employee_name = (By.XPATH,  "//input[@placeholder='Type for hints...']") 
    search_button = (By.XPATH,  "//button[normalize-space()='Search']")
    result_table =  (By.XPATH, "//div[@class='oxd-table-body']")  

    def search_employee(self, name):

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.employee_list)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.employee_name)
        ).send_keys(name)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.result_table)
        )

    