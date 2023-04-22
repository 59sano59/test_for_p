import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
# import unittest

@allure.severity(allure.severity_level.NORMAL)
class tests:
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_developerButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_developers')
        my_element.click()
        
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_qaButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_qa-engineers')
        my_element.click()
        tqa = self.startTime
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_managementButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_management')
        my_element.click()
        tma = self.startTime
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_contact(self):
        driver = self.driver
        driver.get("https:/profilence.com/")
        driver.maximize_window()
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
        driver.get('https:/profilence.com/contact/')
        tcon = self.startTime
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_products(self):
        driver = self.driver
        driver.get("https:/profilence.com/")
        driver.maximize_window()
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
        driver.get('https:/profilence.com/products/')
        tpro = self.startTime
        assert True

if __name__ == "__main__":
    tests()
    
