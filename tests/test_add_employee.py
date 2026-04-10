from pages.login_page import LoginPage
from pages.pim_page import PimPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddEmployee:

    def test_add_employee(self, driver):

        login = LoginPage(driver)
        login.login("Admin", "admin123")

        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )

        pim = PimPage(driver)
        pim.add_employee("John3", "Automation")

        WebDriverWait(driver, 10).until(
            EC.url_contains("viewPersonalDetails")
        )

        assert "viewPersonalDetails".lower() in driver.current_url.lower()