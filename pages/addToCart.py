from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from constants.addToCart_loc import *


@pytest.mark.usefixtures("setup_two")
class AddCart(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
        
        
    def click_search_box(self):
        click_searchBox = self.driver.find_element(By.ID,CLICK_SEARCH_BOX_ID)
        sleep(1)
        click_searchBox.send_keys(SEARCH_DATA)
        
    def click_search_button(self):
        click_searchButton = self.driver.find_element(By.CLASS_NAME,SEARCH_BUTTON_CLASS_NAME)
        click_searchButton.click()
        
    def click_item(self):
        first_item = self.driver.find_element(By.CLASS_NAME,FIRST_ITEM_CLASS_NAME)
        first_item.click()
        
    def click_add_basket_button(self):
        button =self.driver.find_element(By.CLASS_NAME,ADD_BASKET_BUTTON_CLASS_NAME)
        button.click()
        
    def control_add_basket_success(self):
        basket_total = self.driver.find_element(By.XPATH, BASKET_TOTAL)
        basket_total.click()
        
        item = self.driver.find_element(By.CLASS_NAME,ITEM_CLASS_NAME)
        
        href_item = item.get_attribute("href")
        expected_item=EXPECTED_ITEM
        assert href_item == expected_item, f"Expected href to be '{expected_item}' but found '{href_item}'"
