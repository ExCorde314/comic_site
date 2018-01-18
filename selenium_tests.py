import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

WEB_URL = "http://localhost:8000/"

class Comic(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
                        command_executor='http://localhost:9222/wd/hub',
                        desired_capabilities=DesiredCapabilities.CHROME
                )

    def test_home_page(self):
        driver = self.driver
        print("got web driver")
        driver.get(WEB_URL)
        print("got page")
        print(driver.page_source)
        assert "Comedic Cat: " in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    print("Starting Tests")
    unittest.main()
    print("Finished Tests")