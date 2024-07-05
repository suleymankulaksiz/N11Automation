from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.filter_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("setup_two")
class Filter(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def find_category(self):
        menu_category = self.driver.find_element(By.XPATH, FIND_CATEGORY_NAME_H)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_category).perform()
        
    def click_subcategory(self):
        subcategory=self.driver.find_element(By.XPATH,SUBCATEGORY_XPATH)
        subcategory.click()
        
    def brand_selected(self):
        selected_brand_item = self.driver.find_element(By.XPATH,SELECTED_BRAND_ITEM_XPATH)
        selected_brand_item.click()
    
    def processor_model(self):
        selected_brand_name = self.driver.find_element(By.XPATH,SELECTED_BRAND_NAME_XPATH)
        selected_brand_name.click()
        selected_model= self.driver.find_element(By.XPATH,SELECTED_MODEL_XPATH)
        selected_model.click()
        
    def control_filter(self):
        alertMessage = self.driver.find_element(By.XPATH,CONTROL_FILTER_MESSAGE_XPATH).text
        assert alertMessage == CONTROL_EXPECTED_FILTER,CONTROL_EXPECTED_FILTER_ASSERT
        
    def delAllChoiceBtn(self):
        delete_button = self.driver.find_element (By.XPATH,DELETE_BUTTON_XPATH)
        delete_button.click()
    
    def filter_product_result(self):
        filter_result = self.driver.find_element (By.XPATH,FILTER_RESULT_XPATH).text
        assert filter_result == FILTER_RESULT_EXPECTED,FILTER_RESULT_EXPECTED_ASSERT
    
    def filter_after_delete_result(self):
        delete_filter_result = self.driver.find_element(By.XPATH,DELETE_FILTER_RESULT_XPATH).get_attribute("title")
        assert delete_filter_result == DELETE_FILTER_RESULT_EXPECTED,DELETE_FILTER_RESULT_EXPECTED_ASSERT
        
    def click_sorting_dropdown(self):
        element = self.driver.find_element(By.XPATH, CLICK_SORTING_DROPDOWN_XPATH)
        data_value = element.get_attribute("data-value")
        assert data_value == CLICK_SORTING_DROPDOWN_EXPECTED, f"Expected data-value 'NUMARA11' but got '{data_value}'"
        
    def click_price_low(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_low_sorting_box = self.driver.find_element(By.XPATH,CLICK_LOW_SORTING_BOX)
        click_low_sorting_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == ASSERT_MESSAGE_PRICE_LOW, ASSERT_MESSAGE_SORTING_TEXT

    def click_price_high(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_high_sorting_box = self.driver.find_element(By.XPATH,CLICK_HIGH_SORTING_BOX_XPATH)
        click_high_sorting_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == PRICE_HIGH_ASSERT, ASSERT_MESSAGE_SORTING_TEXT

    def click_sales_quantity(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_sales_quantity_box = self.driver.find_element(By.XPATH,CLICK_SALES_QUANTITY_BOX_XPATH)
        click_sales_quantity_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == SALES_QUANTITY_ASSERT, ASSERT_MESSAGE_SORTING_TEXT

    def click_reviews(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_reviews_box = self.driver.find_element(By.XPATH,CLICK_REVIEWS_BOX_XPATH)
        click_reviews_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == REVIEWS_ASSERT, ASSERT_MESSAGE_SORTING_TEXT
    
    def click_new_items(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_newest_box = self.driver.find_element(By.XPATH,CLICK_NEWEST_BOX_XPATH)
        click_newest_box.click()
        
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == NEW_ITEMS_ASSERT, ASSERT_MESSAGE_SORTING_TEXT
        
    def click_review_rate(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_review_rate_box = self.driver.find_element(By.XPATH,CLICK_REVIEW_RATE_BOX_XPATH)
        click_review_rate_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == REVIEW_RATE_ASSERT, ASSERT_MESSAGE_SORTING_TEXT
        
    def click_seller_grade(self):
        click_sorting_box = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH)
        click_sorting_box.click()
        click_seller_grade_box = self.driver.find_element(By.XPATH,CLICK_SELLER_GRADE_XPATH)
        click_seller_grade_box.click()
        assertMessage = self.driver.find_element(By.XPATH,CLICK_SORTING_BOX_XPATH).text
        assert assertMessage == "Sırala: Mağaza Puanı", ASSERT_MESSAGE_SORTING_TEXT
        
    def click_manually_removing_filters(self):
        click_x_button = self.driver.find_element(By.XPATH,CLICK_MANUALLY_REMOVING_FILTERS_XPATH)
        click_x_button.click()
        sleep(1)
        click_x_button_two = self.driver.find_element(By.XPATH,CLICK_X_BUTTON_TWO)
        click_x_button_two.click()
        self.driver.save_screenshot("images/manuallyRemovingFiltersResult.png")
        
    def click_delivery_location(self):
        location_button = self.driver.find_element(By.XPATH,LOCATION_BUTTON_XPATH)
        location_button.click()
        sleep(2)
      
    def click_location_city(self):
        sleep(2)
        select_city = self.driver.find_element(By.CSS_SELECTOR, SELECT_CITY_CSS)
        select_city_dropdown=Select(select_city)
        select_city_dropdown.select_by_value("2534")
        
    def click_location_(self):
        sleep(2)
        select_district = self.driver.find_element(By.CSS_SELECTOR, SELECT_DISTRICT_CSS)
        select_district_dropdown=Select(select_district)
        select_district_dropdown.select_by_value("22812")
                
    def click_my_location_btn(self):
        clickLocation_btn = self.driver.find_element(By.XPATH,CLICK_LOCATION_BTN_XPATH)
        clickLocation_btn.click()
        sleep(2)
        
    def control_location(self):
        location_name = self.driver.find_element(By.XPATH,LOCATION_NAME_XPATH).text
        assert location_name ==LOCATION_NAME_TEXT,LOCATION_NAME__ASSERT_TEXT

    def my_location_panel_button(self):
        
        myLocationBtn=self.driver.find_element(By.XPATH,MY_LOCATION_BTN_XPATH)
        myLocationBtn.click()
        
    def click_myLocationBtn_city(self):
        sleep(2)
        myLocationBtnCity= self.driver.find_element(By.XPATH,MY_LOCATION_BTN_CITY_XPATH)
        myLocationBtnCity_select = Select(myLocationBtnCity)
        myLocationBtnCity_select.select_by_value("2534")
               
    def click_myLocationBtn_district(self):
        sleep(2)
        myLocationBtnDistrict= self.driver.find_element(By.XPATH,MY_LOCATION_BTN_DISTRICT_XPATH)
        myLocationBtnDistrict_select = Select(myLocationBtnDistrict)
        myLocationBtnDistrict_select.select_by_value("22812")
    
    def click_myLocationBtn_top_button(self):
        top_my_location_button = self.driver.find_element (By.XPATH,TOP_MY_LOCATION_XPATH)
        top_my_location_button.click()
    
    def control_location_panel(self):
        control_switch_button = self.driver.find_element(By.XPATH,CONTROL_SWITCH_BUTTON_XPATH)
        assert not control_switch_button.is_enabled(), CONTROL_LOCATION_PANEL_ASSERT
    
    def click_search_box(self):
        click_searchBox = self.driver.find_element(By.ID,CLICK_SEARCH_BOX_ID)
        click_searchBox.send_keys("Macbook air")
        
    def click_search_button(self):
        click_searchButton = self.driver.find_element(By.CLASS_NAME,SEARCH_BUTTON_CLASS_NAME)
        click_searchButton.click()
        
    def control_search_box_list(self):
        link = self.driver.find_element(By.XPATH, CONTROL_SEARCH_BOX_XPATH)
        expected_href = EXPECTED_URL_SEARCH_BOX
        actual_href = link.get_attribute("href")
        assert actual_href == expected_href, f"Link href beklenen değerden farklı: {actual_href}"
        
    def click_location_specific_delivery(self):
        location_specific_button = self.driver.find_element(By.XPATH,CLICK_LOCATION_SPECIFIC_DELIVERY_XPATH)
        location_specific_button.click()
    
    def click_same_day_delivery(self):
        same_day_button = self.driver.find_element(By.XPATH,CLICK_SAME_DAY_DELIVERY_XPATH)
        same_day_button.click()
    
    def control_specific_location_filters(self):
        self.driver.save_screenshot("images/Specific_LocationFiltersResult.png")
    
    def click_campaignFilter(self):
        click_campaign = self.driver.find_element(By.XPATH,CLICK_CAMPAIGN_FILTER_XPATH)
        click_campaign.click()
        
    def click_gift_campaigns_checkbox(self):
        click_gift_campigns = self.driver.find_element(By.XPATH, CLICK_GIFT_CAMPAIGNS_CHECHBOX_XPATH)
        click_gift_campigns.click()
    
    def click_instant_discount_heckbox(self):
        click_instant_discount = self.driver.find_element(By.XPATH, CLICK_INSTANT_DISCOUNT_XPATH)
        click_instant_discount.click()
        
    def control_campaignFilter(self):
        expected_url_campaignFilter = "https://www.n11.com/arama?q=Macbook+air&hscp=hediyeli-kampanya_anlik-indirim&hdfl=cats_camps_m_ppf"
        current_url = self.driver.current_url

        assert current_url == expected_url_campaignFilter, f"URL does not match expected URL. Expected: {expected_url_campaignFilter}"