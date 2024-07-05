from time import sleep
from selenium import webdriver
import pytest
from pages.addToCart import *

@pytest.mark.usefixtures("setup_two")
class TestAddCart:
    
    
    def test_add_item_to_cart(self):
        add = AddCart(self.driver)
        add.click_search_box()
        add.click_search_button()
        add.click_item()
        add.click_add_basket_button()
        add.control_add_basket_success()
    
    