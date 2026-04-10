from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditEmployee:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    save_btn = (By.XPATH, "//button[@type='submit']")

    def edit_employee(self, firstname, lastname):

        first = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.first_name)
        )

        first.clear()
        first.send_keys(firstname)

        last = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.last_name)
        )

        last.clear()
        last.send_keys(lastname)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.save_btn)
        ).click()    
        