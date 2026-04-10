from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEmployeeList():

    def test_search_employee(self, driver):

        login = LoginPage(driver)
        login.login("Admin", "admin123")

        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard")
        )

        employee = EmployeeListPage(driver)
        employee.search_employee("John")

        assert "pim/viewEmployeeList" in driver.current_url