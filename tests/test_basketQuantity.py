from time import sleep
from selenium import webdriver
import pytest
from pages.basketQuantity import *


@pytest.mark.usefixtures("setup_two")
class TestBasketQuantity:
    
    def test_basket_product_quantity_plus_button(self):
        quantity = BasketQuantity(self.driver)
        quantity.click_search_box()
        quantity.click_search_button()
        quantity.click_item()
        quantity.click_add_basket_button()
        quantity.control_add_basket_success()
        quantity.click_increase_product_quantity()
        
    def test_decrease_product_quantity_button_cart(self):
        quantity = BasketQuantity(self.driver)
        self.test_basket_product_quantity_plus_button()
        quantity.Press_the_minus_button()
        
        
    def test_allowed_maximum_product_quantity(self):
        quantity = BasketQuantity(self.driver)
        quantity.click_search_box()
        quantity.click_search_button()
        quantity.click_item()
        quantity.click_add_basket_button()
        quantity.control_add_basket_success()
        quantity.click_beyond_the_allowed_limit()
        quantity.check_the_warning_message()
    
    def test_add_multiple_products_to_the_basket(self):
        quantity = BasketQuantity(self.driver)
        quantity.click_search_box()
        quantity.click_search_button()
        quantity.click_item()
        quantity.click_add_basket_button()
        quantity.open_the_basket()
        quantity.add_a_new_product()
        quantity.check_the_updated_basket()
        
        
    def test_remove_item_from_the_basket(self):
        quantity = BasketQuantity(self.driver)
        quantity.add_a_new_product()
        quantity.click_on_the_trash_icon()
        quantity.click_delete_button()
        quantity.verify_that_the_item_has_been_deleted_from_the_cart()

    def test_deleting_item_from_the_cart_and_adding_to_favorites(self):
        quantity = BasketQuantity(self.driver)
        quantity.add_a_new_product()
        quantity.click_on_the_trash_icon()
        quantity.click_delete_and_add_to_favorites_button()
        quantity.click_add_favorite_button()
        quantity.confirm_that_the_deleted_product_is_added_to_favorites()
        






        