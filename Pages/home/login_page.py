import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):
    
    # locators
    _sing_log = '//div[contains(text(),"Sign Up or Log In")]'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = '//input[@class="btn btn-default btn-block btn-md dynamic-button"]'
    _verify_login = '//span[@class="dynamic-text help-block"]'
    
    
    def __init__(self, driver):
        self.driver = driver
    
    def test_login(self):
        baseUrl = 'https://letskodeit.com/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
    
    def singLog(self):
        self.driver.find_element(By.XPATH, self._sing_log)
    
    def emailField(self):
        self.driver.find_element(By.ID, self._email_field)    
    
    def passwordField(self):
        self.driver.find_element(By.ID, self._password_field)            
    
    def loginButton(self):
        self.driver.find_element(By.XPATH, self._login_button)
    
    
    def clickLogIn(self):
        self._sing_log.click()
    
    def enterEmail(self):
        self._email_field.clear()
        self._email_field.send_keys('test@email.com')     

    def enterPassword(self):
        self._password_field.clear()
        self._password_field.send_keys('abcabc')
    
    def clickButton(self):
        self._login_button.click()        

    def Login(self):
        self.test_login()
                
        self.singLog()
        self.clickLogIn()
        
        self.emailField()
        self.enterEmail()
        
        self.passwordField()
        self.enterPassword()
        
        self.loginButton()
        self.clickButton()
    
    def test_verifyLogin(self):
        assert self._verify_login == 'Your username or password is invalid. Please try again.'
        
        self.driver.quit()
