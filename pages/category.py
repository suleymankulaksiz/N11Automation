from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from constants.category_loc import *


@pytest.mark.usefixtures("setup_two")
class Category(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    
        
    def find_category(self):
        
        menu_element = self.driver.find_element(By.XPATH, find_category_name)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()
        
    def click_category(self):
        click_category_button = self.driver.find_element (By.XPATH,CLICK_CATEGORY_BUTTON_XPATH)
        click_category_button.click()
        
    def control_category_name(self):
        category_name = self.wait_for_element_visible(By.XPATH,CATEGORY_NAME_XPATH).get_attribute("title")
        assert category_name == CATEGORY_NAME_TEXT, CONTROL_CATEGORY_NAME_ASSERT
        
    def click_category_two(self):
        clickable_category = self.driver.find_element (By.XPATH,CLICKABLE_CATEGORY_XPATH)
        clickable_category.click()
        
    def click_subcategory(self):
        subcategory=self.driver.find_element(By.XPATH,SUBCATEGORY_XPATH)
        subcategory.click()
        
    def control_subcategory_name(self):
        category_name = self.driver.find_element (By.XPATH,SUBCATEGORY_NAME_XPATH).get_attribute("title")
        assert category_name ==CATEGORY_NAME_TWO,CATEGORY_NAME_TEXT_ASSERT
        
    def click_brand_category(self):
        brand_name_click= self.driver.find_element(By.XPATH,BRAND_NAME_CLICK_XPATH)
        brand_name_click.click()
    
    def control_brand_name(self):
        find_brand_name = self.driver.find_element (By.XPATH,CONTROL_BRAND_NAME_XPATH).text
        assert find_brand_name == FIND_BRAND_NAME,BRAND_NAME_TEXT_ASSERT