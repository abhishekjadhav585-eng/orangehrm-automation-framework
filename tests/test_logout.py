from pages.pim_page import PimPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()

class TestLogout():

    def test_logout(self, driver):

        logger.info("Test Started: Logout Flow")

        login = LoginPage(driver)
        logger.info("Logging into application")
        login.login( "Admin", "admin123")

        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )
        logger.info("Login successful, dashboard loaded")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(("xpath", "//span[text()='PIM']"))
        )

        pim = PimPage(driver)
        logger.info("adding new employee")
        pim.add_employee("John3", "Automation")

        WebDriverWait(driver, 20).until(
            EC.url_contains("viewPersonalDetails")
        )
        logger.info("employee added succesfully")

        logout = DashboardPage(driver)
        logger.info("logging out from application")
        logout.logout()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        logger.info("logged out succesfully")
        
        assert "login" in driver.current_url.lower()