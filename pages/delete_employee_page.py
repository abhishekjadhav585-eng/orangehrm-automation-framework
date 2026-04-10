from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteEmployee():

    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    employee_list = (By.XPATH,"//a[normalize-space()='Employee List']")
    delete_button = (By.XPATH,  "(//i[@class='oxd-icon bi-trash'])[1]") 
    confirm_delete = (By.XPATH, "//button[normalize-space()='Yes, Delete']") 

    def delete_first_employee(self):

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.employee_list)
        ).click() 

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.confirm_delete)
        ).click() 
        