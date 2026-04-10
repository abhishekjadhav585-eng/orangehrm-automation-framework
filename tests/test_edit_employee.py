from pages.login_page import LoginPage
from pages.employee_search_page import SearchEmployee
from pages.edit_employee_page import EditEmployee
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEditEmployee:

    def test_edit_employee(self, driver):

        login = LoginPage(driver)
        login.login("Admin", "admin123")

        search = SearchEmployee(driver)
        search.search_employee("John")
        search.click_employee()

        edit =EditEmployee(driver)
        edit.edit_employee("Johnny", "Doe")

        assert "viewPersonalDetails" in driver.current_url