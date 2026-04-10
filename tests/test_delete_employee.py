from pages.login_page import LoginPage
from pages.delete_employee_page import DeleteEmployee
from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()

class TestDeleteEmployee():

    def test_delete_employee(self, driver):

        logger.info("test started: delete first employee ")

        login = LoginPage(driver)
        logger.info("logging into application")
        login.login("Admin", "admin123")

        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard")
        )
        logger.info("Login successful, dashboard loaded")

        delete_emp = DeleteEmployee(driver)
        logger.info("deleting first employee")
        delete_emp.delete_first_employee()

        logger.info("employee deleted succesfully")

        assert "viewEmployeeList" in driver.current_url