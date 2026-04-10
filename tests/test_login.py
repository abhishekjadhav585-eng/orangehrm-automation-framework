from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_valid_login(self, driver):

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )


        assert "dashboard" in driver.current_url.lower()

