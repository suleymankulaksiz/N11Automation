from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.login_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *

@pytest.mark.usefixtures("setup")
class Login(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
   
  
    def click_loginButton(self):
        target = self.driver.find_element(By.XPATH,CLICK_LOGIN)
        target.click()
        sleep(5)
        
    def click_email(self):
        target = self.driver.find_element(By.XPATH,CLICK_EMAIL)
        target.send_keys(email_info)
        
    def click_password(self):
        target = self.driver.find_element(By.XPATH,CLICK_PASSWORD)
        target.send_keys(password_info)
        
    def click_Button(self):
        target = self.driver.find_element(By.XPATH,CLICK_LOGIN_BUTTON)
        target.click()
        sleep(2)
        
    def fail_password(self):
        target = self.driver.find_element(By.XPATH,CLICK_PASSWORD)
        target.send_keys(fail_password_info)
    
    def fail_text(self):
        alertMessage = self.wait_for_element_visible(By.XPATH, FAIL_TEXT_XPATH)
        assert alertMessage.text == FAIL_TEXT
        
    def fail_email(self):
        target = self.driver.find_element(By.XPATH,CLICK_EMAIL)
        target.send_keys(fail_email_info)
        
    def iformat_email(self):
        target = self.driver.find_element(By.XPATH,CLICK_EMAIL)
        target.send_keys(invalid_format_email)
        
    def alert_email(self):
        alertMessage = self.wait_for_element_visible(By.XPATH,FAIL_EMAIL_XPATH)
        assert alertMessage.text == FAIL_EMAIL_TEXT
    
    def masked_password(self):
        password_type = self.wait_for_element_visible(By.XPATH,CLICK_PASSWORD).get_attribute("type")
        assert password_type == MASKED_ASSERT, MASKED_ASSERT_TEXT
    
    def control_login(self):
        sleep(2)
        myAccount= self.wait_for_element_visible(By.XPATH,CONTROL_LOGIN_MY_ACCOUNT_XPATH).get_attribute("title")
        assert myAccount == CONTROL_LOGIN_ASSERT,CONTROL_LOGIN_ASSERT_TEXT
        
        
        

    
