from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.products_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("setup_two")
class Products(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
        
        
    def click_search_box(self):
        click_searchBox = self.driver.find_element(By.ID,CLICK_SEARCH_BOX_ID)
        click_searchBox.send_keys("Macbook air")
        
    def click_search_button(self):
        click_searchButton = self.driver.find_element(By.CLASS_NAME,SEARCH_BUTTON_CLASS_NAME)
        click_searchButton.click()
        
    def click_first_item(self):
        click_item= self.driver.find_element(By.XPATH,CLICK_FIRST_ITEM_XPATH)
        click_item.click()
        
    def control_list_product(self):
        
        item_target = self.driver.find_element(By.CLASS_NAME, ITEM_TARGET_CLASS_NAME)
        first_product_title = item_target.get_attribute("title")
        item_target.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains(ITEM_NAME))
        second_product_title = self.driver.find_element(By.XPATH, SECOND_PRODUCT_TITLE).text
        assert first_product_title == second_product_title, f"Titles do not match. Expected: '{first_product_title}', Actual: '{second_product_title}'"
    
    def more_product_features(self):
        click_more_features = self.driver.find_element(By.XPATH,MORE_PRODUCT_FEATURES)
        click_more_features.click()
        
    def review_products(self):
    
        product_review =self.driver.find_element(By.ID,REVIEW_PRODUCT_ID)
        product_review.click()
    
    def star_rating(self):
        stars_four = self.driver.find_element(By.XPATH,STARS_FOUR_XPATH)
        stars_four.click()
        stars_five=self.driver.find_element(By.XPATH,STARS_FIVE_XPATH)
        stars_five.click()
        
    def control_rating_star(self):
        rating_star_target = self.wait_for_element_visible(By.XPATH,RATING_STAR_TARGET).text
        assert rating_star_target ==STAR_ASSERT , ASSERT_STAR_TEXT
        
    def cargo_details(self):
        detailPreviewBtn = self.driver.find_element(By.CLASS_NAME,CARGO_DETAILS_BUTTON_CLASS_NAME)
        text_btn_name = detailPreviewBtn.text
        assert text_btn_name == CARGO_DETAILS_BUTTON_ASSERT,CARGO_DETAILS_BUTTON_TEXT
        detailPreviewBtn.click()
        
    def cargo_details_window_close(self):
        sleep(2)
        close_button = self.driver.find_element(By.XPATH,CARGO_DETAILS_WINDOW_CLOSE_XPATH)
        close_button.click()








