from time import sleep
from selenium import webdriver
import pytest
from pages.category import *

@pytest.mark.usefixtures("setup_two")
class TestCategory:
    
    
    
    def test_listing_products_category(self):
        category = Category(self.driver)
        category.find_category()
        category.click_category()
        category.control_category_name()
        
    def test_listing_subcategories(self):
        category = Category(self.driver)
        category.click_category_two()
        category.click_subcategory()
        category.control_subcategory_name()
        
    def test_categorize_brand_name(self):
        category = Category(self.driver)
        category.click_category_two()
        category.click_brand_category()
        category.control_brand_name()
        
        