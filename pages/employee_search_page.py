from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchEmployee():
    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    search_box = (By.XPATH, "//input[@placeholder='Type for hints...']") 
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    employee_name_link = (By.XPATH, "//div[@role='rowgroup']//div[1]//div[1]//div[2]") 

    def search_employee(self, name):

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.search_box)
        ).send_keys(name)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()


    def click_employee(self):

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']"))
        )

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.employee_name_link)
        ).click()    