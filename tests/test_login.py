from time import sleep
from selenium import webdriver
import pytest
from pages.login import *

@pytest.mark.usefixtures("setup")
class TestLogin:
    


    def test_successful_login(self):
        login = Login(self.driver)
        login.click_loginButton()
        login.click_email()
        login.click_password()
        login.click_Button()
        login.control_login()
       
    def test_failed_password_login(self):
        login = Login(self.driver)
        login.click_loginButton()
        login.click_email()
        login.fail_password()
        login.click_Button()
        login.fail_text()
        
    def test_failed_email_login(self):
        login = Login(self.driver)
        login.click_loginButton()
        login.fail_email()
        login.click_password()
        login.click_Button()
        login.fail_text()
        
        
    def test_invalid_format_email(self):
        login = Login(self.driver)
        login.click_loginButton()
        login.iformat_email()
        login.click_password()
        login.alert_email()
        
        
    def test_masked_password(self):
        login = Login(self.driver)
        login.click_loginButton()
        login.click_email()
        login.click_password()
        login.masked_password()
        
        
        
        
        
