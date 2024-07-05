from time import sleep
from selenium import webdriver
from constants.login_loc import *
import pytest
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By




@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
    
    
@pytest.fixture(scope="class")
def setup_two(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    sleep(2)#cookies
    l1 = driver.find_element(By.XPATH,CLICK_LOGIN)
    l1.click()
    l2 = driver.find_element(By.XPATH,CLICK_EMAIL)
    l2.send_keys(email_info)
    l3 = driver.find_element(By.XPATH,CLICK_PASSWORD)
    l3.send_keys(password_info)
    l4 = driver.find_element(By.XPATH,CLICK_LOGIN_BUTTON)
    l4.click()
    request.cls.driver = driver
    yield
    driver.quit()