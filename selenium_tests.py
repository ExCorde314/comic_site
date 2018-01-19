import sys
import argparse
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

WEB_URL = "http://localhost:8000/"

TRAVIS = False

def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    if TRAVIS:
        return webdriver.Chrome('./chromedriver', options=options)
    else:
        return webdriver.Chrome('./chromedriver.exe', options=options)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', default='non_travis')
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()

    if args.env == 'travis':
        TRAVIS = True
    else:
        TRAVIS = False

    sys.argv[1:] = args.unittest_args

    unittest.main()