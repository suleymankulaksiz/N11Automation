from time import sleep, time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from constants.basketQuantity_loc import *


@pytest.mark.usefixtures("setup_two")
class BasketQuantity(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def click_search_box(self):
        click_searchBox = self.driver.find_element(By.ID,CLICK_SEARCH_BOX_ID)
        sleep(1)
        click_searchBox.send_keys(SEARCH_BOX_ITEM_NAME)
        
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
        expected_item="https://www.n11.com/urun/samsung-galaxy-a05s-4-gb-128-gb-samsung-turkiye-garantili-47963017?magaza=n11"
        assert href_item == expected_item, f"Expected href to be '{expected_item}' but found '{href_item}'"
    
    
    def click_increase_product_quantity(self):
        self.driver.save_screenshot("images/CartPriceBeforePressingThePlusButton.png")

        plus_button = self.driver.find_element(By.XPATH,PLUS_BUTTON_XPATH)
        plus_button.click()
        sleep(2)
        self.driver.save_screenshot("images/CartPriceAfterPressingThePlusButton.png")
        
    def Press_the_minus_button(self):
        click_minus = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[1]/div[1]/div[3]/section/table[2]/tbody/tr/td[1]/div[3]/div[2]/div/span[2]")
        click_minus.click()
        sleep(2)
        self.driver.save_screenshot("images/AfterPressingTheMinusButton.png")

    def click_beyond_the_allowed_limit(self):
        plus_button = self.driver.find_element(By.XPATH,PLUS_BUTTON_XPATH)
        plus_button.click()
        plus_button.click()
        plus_button.click()
        
    def check_the_warning_message(self):
        sleep(2)
        warnig_message = self.driver.find_element(By.XPATH,"/html/body/div[7]/div/span[2]").text
        assert warnig_message ==WARNING_MESSAGE_EXPECTED,f"Warning message does not match the expected: {warnig_message}"
    
    def open_the_basket(self):
        basket_total = self.driver.find_element(By.XPATH, BASKET_TOTAL)
        basket_total.click()
        
        basket_items_count = self.driver.find_element(By.XPATH,BASKET_ITEMS_COUNT_XPATH).text
        assert basket_items_count ==BASKET_ITEMS_COUNT_EXPECTED,BASKET_ITEMS_COUNT_ASSERT

    def add_a_new_product(self):
        click_searchBox = self.driver.find_element(By.ID,CLICK_SEARCH_BOX_ID)
        click_searchBox.send_keys(ADD_NEW_ITEM_NAME)
        click_searchButton = self.driver.find_element(By.CLASS_NAME,SEARCH_BUTTON_CLASS_NAME)
        click_searchButton.click()
        add_new_item = self.driver.find_element(By.XPATH,ADD_NEW_ITEM_XPATH)
        add_new_item.click()
        button =self.driver.find_element(By.CLASS_NAME,ADD_BASKET_BUTTON_CLASS_NAME)
        button.click()
        basket_total = self.driver.find_element(By.XPATH, BASKET_TOTAL)
        basket_total.click()
        
        sleep(2)
    
    def check_the_updated_basket(self):
        
        new_basket_items_count = self.driver.find_element(By.XPATH,NEW_BASKET_ITEMS_COUNT_XPATH).text
        assert new_basket_items_count ==NEW_BASKET_ITEMS_COUNT_EXPECTED,NEW_BASKET_ITEMS_COUNT_ASSERT
        
    def click_on_the_trash_icon(self):
        trash = self.driver.find_element(By.XPATH,CLICK_TRASH_ICON)
        trash.click()
    
    def click_delete_button(self):
        delete_btn = self.driver.find_element(By.XPATH,DELETE_BUTTON)
        delete_btn.click()
        
    def verify_that_the_item_has_been_deleted_from_the_cart(self):
        sleep(2)
        control_basket = self.driver.find_element(By.XPATH,CONTROL_BASKET).text
        assert control_basket == EXPECTED_CONTROL_BASKET,ASSERT_CONTROL_BASKET
    
    def click_delete_and_add_to_favorites_button(self):
        sleep(2)
        delete_and_favorite_btn = self.driver.find_element(By.XPATH,DELETE_AND_FAVORITE_BUTTON)
        delete_and_favorite_btn.click()
        sleep(2)

    def click_add_favorite_button(self):
        favorite_btn = self.driver.find_element(By.XPATH,FAVORITE_BUTTON_XPATH)
        sleep(2)
        favorite_btn.click()
        
    def confirm_that_the_deleted_product_is_added_to_favorites(self):
        control_favorite = self.driver.find_element(By.XPATH,CONTROL_FAVORITE_XPATH).text
        assert control_favorite == CONTROL_FAVORITE_ITEM,ASSERT_FAVORITE_ITEM


























            
        










        
        