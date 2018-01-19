import sys
import argparse
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

WEB_URL = "http://localhost:8000/"
DRIVER_LOC = './chromedriver.exe'

def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    return webdriver.Chrome(DRIVER_LOC, options=options)

class ComicTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_web_driver()

    def test_home_page(self):
        driver = self.driver
        driver.get(WEB_URL)
        assert "Comedic Cat: " in driver.page_source
        assert "comic-container" in driver.page_source

    def test_single(self):
        driver = self.driver
        driver.get(WEB_URL + '1')
        assert "Comedic Cat: " in driver.page_source
        assert "comic-container" in driver.page_source
        assert 'Finding A Hat' in driver.page_source

    def tearDown(self):
        self.driver.quit()

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_web_driver()

    def test_home_page(self):
        driver = self.driver
        driver.get(WEB_URL + 'blog')
        assert "Comedic Cat: " in driver.page_source
        assert "blog-container" in driver.page_source

    def test_single(self):
        driver = self.driver
        driver.get(WEB_URL + 'blog/1')
        assert "Comedic Cat: " in driver.page_source
        assert "blog-container" in driver.page_source
        assert 'Hello World!' in driver.page_source

    def tearDown(self):
        self.driver.quit()

class AdminSignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_web_driver()

    def test_get_signup_page(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source

    def test_signup(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source
        element = driver.find_element_by_id("id_first_name")
        element.clear()
        element.send_keys("Jonathan")
        element = driver.find_element_by_id("id_last_name")
        element.clear()
        element.send_keys("Lowe")
        element = driver.find_element_by_id("id_email")
        element.clear()
        element.send_keys("comediccatcomic@gmail.com")
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ComedicCat")
        element = driver.find_element_by_id("id_password1")
        element.clear()
        element.send_keys("password")
        element = driver.find_element_by_id("id_password2")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/admin-panel' == driver.current_url

    def test_signup_invalid_form_1(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source
        element = driver.find_element_by_id("id_first_name")
        element.clear()
        element.send_keys("")
        element = driver.find_element_by_id("id_last_name")
        element.clear()
        element.send_keys("Lowe")
        element = driver.find_element_by_id("id_email")
        element.clear()
        element.send_keys("jonathanglowe@gmail.com")
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element = driver.find_element_by_id("id_password1")
        element.clear()
        element.send_keys("")
        element = driver.find_element_by_id("id_password2")
        element.clear()
        element.send_keys("")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/signup' == driver.current_url
        assert 'This field is required.' in driver.page_source

    def test_signup_invalid_form_2(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source
        element = driver.find_element_by_id("id_first_name")
        element.clear()
        element.send_keys("Jonathan")
        element = driver.find_element_by_id("id_last_name")
        element.clear()
        element.send_keys("Lowe")
        element = driver.find_element_by_id("id_email")
        element.clear()
        element.send_keys("comediccatcomic@gmail.com")
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element = driver.find_element_by_id("id_password1")
        element.clear()
        element.send_keys("password")
        element = driver.find_element_by_id("id_password2")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/signup' == driver.current_url
        assert 'Username already exists.' in driver.page_source

    def test_signup_invalid_form_3(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source
        element = driver.find_element_by_id("id_first_name")
        element.clear()
        element.send_keys("Jonathan")
        element = driver.find_element_by_id("id_last_name")
        element.clear()
        element.send_keys("Lowe")
        element = driver.find_element_by_id("id_email")
        element.clear()
        element.send_keys("jonathanglowe@gmail.com")
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element = driver.find_element_by_id("id_password1")
        element.clear()
        element.send_keys("password1")
        element = driver.find_element_by_id("id_password2")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/signup' == driver.current_url
        assert 'Passwords do not match.' in driver.page_source

    def test_signup_invalid_form_4(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/signup')
        assert 'Sign Up' in driver.page_source
        assert 'form-signup' in driver.page_source
        element = driver.find_element_by_id("id_first_name")
        element.clear()
        element.send_keys("Jonathan")
        element = driver.find_element_by_id("id_last_name")
        element.clear()
        element.send_keys("Lowe")
        element = driver.find_element_by_id("id_email")
        element.clear()
        element.send_keys("jonathanglowe1@gmail.com")
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde31445")
        element = driver.find_element_by_id("id_password1")
        element.clear()
        element.send_keys("password")
        element = driver.find_element_by_id("id_password2")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/signup' == driver.current_url
        assert 'Email not authorized.' in driver.page_source

    def tearDown(self):
        self.driver.quit()

class AdminLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_web_driver()

    def test_get_login_page(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/login')
        assert 'Log In' in driver.page_source
        assert 'form-signin' in driver.page_source

    def test_login_success(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/login')
        assert 'Log In' in driver.page_source
        assert 'form-signin' in driver.page_source
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element = driver.find_element_by_id("id_password")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/' == driver.current_url

    def test_login_invalid_1(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/login')
        assert 'Log In' in driver.page_source
        assert 'form-signin' in driver.page_source
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde3141")
        element = driver.find_element_by_id("id_password")
        element.clear()
        element.send_keys("password")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/login' == driver.current_url
        assert 'The username or password is invalid' in driver.page_source

    def test_login_invalid_2(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/login')
        assert 'Log In' in driver.page_source
        assert 'form-signin' in driver.page_source
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element = driver.find_element_by_id("id_password")
        element.clear()
        element.send_keys("passwordd")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/login' == driver.current_url
        assert 'The username or password is invalid' in driver.page_source

    def test_login_invalid_3(self):
        driver = self.driver
        driver.get(WEB_URL + 'access-portal/login')
        assert 'Log In' in driver.page_source
        assert 'form-signin' in driver.page_source
        element = driver.find_element_by_id("id_username")
        element.clear()
        element.send_keys("ExCorde314")
        element.send_keys(Keys.RETURN)

        assert WEB_URL + 'access-portal/login' == driver.current_url
        assert 'This field is required.' in driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--driver', default='./chromedriver.exe')
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()

    DRIVER_LOC = args.driver

    sys.argv[1:] = args.unittest_args

    unittest.main()