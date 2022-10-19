from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.register_page import RegisterPage
import unittest
import time

class RegisterTest(unittest.TestCase):
    
    baseUrl = 'https://courses.letskodeit.com/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    rp = RegisterPage(driver)
    
    def test_registerPage(self):
        self.driver.get(self.baseUrl)
        self.rp.registerCourse('JavaScript for beginners')
        self.rp.card('1234 2345 3456 4567', '10/24', '345') 
        self.rp.country('Poland')
        
        message = self.rp.errorCardNumber()
        assert message == 'Numer karty jest nieprawidłowy.' 
        
        self.driver.quit()

