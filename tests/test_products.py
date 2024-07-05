from time import sleep
from selenium import webdriver
import pytest
from pages.products import *

@pytest.mark.usefixtures("setup_two")
class TestProducts:
    
    def test_user_product_selection(self):
        item = Products(self.driver)
        item.click_search_box()
        item.click_search_button()
        item.control_list_product()
    
    def test_product_details(self):
        item = Products(self.driver)
        self.test_user_product_selection()
        item.more_product_features()
    
    def test_product_options(self):
        item = Products(self.driver)
        self.test_user_product_selection()
        item.review_products()
        item.star_rating()
        item.control_rating_star()
    
    def test_cargo_details(self):
        item = Products(self.driver)
        self.test_user_product_selection()
        item.cargo_details()
        item.cargo_details_window_close()
