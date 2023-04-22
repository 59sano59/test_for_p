from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import json
import time
import pandas as pd
import unittest

class tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
        assert True


    def test_developerButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_developers')
        my_element.click()
        
        assert True

    def test_qaButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_qa-engineers')
        my_element.click()
        tqa = self.startTime
        assert True

    def test_managementButton(self):
        driver = self.driver
        driver.get("https:/profilence.com/products/")
        driver.maximize_window()
        my_element = driver.find_element(By.ID, 'tabby-toggle_management')
        my_element.click()
        tma = self.startTime
        assert True

    def test_contact(self):
        driver = self.driver
        driver.get("https:/profilence.com/")
        driver.maximize_window()
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
        driver.get('https:/profilence.com/contact/')
        tcon = self.startTime
        assert True

    def test_products(self):
        driver = self.driver
        driver.get("https:/profilence.com/")
        driver.maximize_window()
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
        driver.get('https:/profilence.com/products/')
        tpro = self.startTime
        assert True

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(tests)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
