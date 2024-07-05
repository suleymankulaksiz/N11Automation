from time import sleep
from selenium import webdriver
import pytest
from pages.filtering import *

@pytest.mark.usefixtures("setup_two")
class TestFiltering:
    
    def test_find_category_menu(self):
        filter = Filter(self.driver)
        filter.find_category()
        filter.click_subcategory()
        filter.brand_selected()
        filter.processor_model()
        filter.control_filter()
        
    def test_clear_filter_button(self):
        filter = Filter(self.driver)
        self.test_find_category_menu()
        filter.filter_product_result()
        filter.delAllChoiceBtn()
        filter.filter_after_delete_result()
        
    def test_sorting_dropdown(self):
        filter = Filter(self.driver)
        self.test_find_category_menu()
        filter.click_sorting_dropdown()
        filter.click_price_low()
        filter.click_price_high()
        filter.click_sales_quantity()
        filter.click_reviews()
        filter.click_new_items()
        filter.click_review_rate()
        filter.click_seller_grade()
        
    def test_manually_removing_filters(self):
        filter = Filter(self.driver)
        self.test_find_category_menu()
        filter.click_manually_removing_filters()
        
    def test_delivery_location_filter(self):
        filter = Filter(self.driver)
        filter.find_category()
        filter.click_subcategory()
        filter.click_delivery_location()
        filter.click_location_city()
        filter.click_location_()
        filter.click_my_location_btn()
        filter.control_location()

    def test_delivery_location_panel_filter(self):
        filter = Filter(self.driver)
        self.test_find_category_menu()
        filter.my_location_panel_button()
        filter.click_myLocationBtn_city()
        filter.click_myLocationBtn_district()
        filter.click_myLocationBtn_top_button()
        filter.control_location_panel()
        
    def test_search_box_list(self):
        filter = Filter(self.driver)
        filter.click_search_box()
        filter.click_search_button()
        filter.control_search_box_list()
    
    def test_location_specific_filters(self):
        filter=Filter(self.driver)
        self.test_search_box_list()
        filter.click_delivery_location()
        filter.click_location_city()
        filter.click_location_()
        filter.click_my_location_btn()
        filter.click_location_specific_delivery()
        filter.click_same_day_delivery()
        filter.control_specific_location_filters()
        
    def test_listing_promotional_products(self):
        filter=Filter(self.driver)
        self.test_search_box_list()
        filter.click_campaignFilter()
        filter.click_gift_campaigns_checkbox()
        filter.click_instant_discount_heckbox()
        filter.control_campaignFilter()
