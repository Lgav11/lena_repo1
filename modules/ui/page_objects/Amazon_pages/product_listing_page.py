from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class ProductListingPage(BasePage):
    URL = "https://www.amazon.com/ref=nav_logo"

    def __init__(self) -> None:
        super().__init__()

    def navigate_to(self):
        self.driver.get(ProductListingPage.URL)

    def search_product(self, product_name):
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys(product_name)
        search_btn_elem = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_btn_elem.click()

    def verify_title(self, correct_title):
        return self.driver.title == correct_title

    def verify_result_info_bar(self, product_name):  # find result info bar
        find_result_info_bar = self.driver.find_element(
            By.XPATH, "//span[contains(@class,'a-color-state')]"
        )
        return find_result_info_bar.text.strip('"') == product_name

    def verify_language_picker_in_header(self):  # find language picker
        lang_picker = self.driver.find_element(By.ID, "icp-nav-flyout")
        lang_picker.click()

    def customer_reviews_filter(self):
        customer_review_block = self.driver.find_element(By.ID, "reviewsRefinements")
        choose_customer_review_filter = self.driver.find_element(
            By.XPATH, "//i[@class='a-icon a-icon-star-medium a-star-medium-4']"
        )
        choose_customer_review_filter.click()

    def clear_link_option_customer_reviews_filter(self):
        find_clear_link = self.driver.find_element(
            By.XPATH,
            "//span[text()='Clear']/ancestor::div[@id='reviewsRefinements']",
        )
        is_present = find_clear_link.is_enabled()
        return is_present


"""
    def brands_filter_selection(self):
        find_brand_filter_checkbox = self.driver.find_element(
            By.XPATH,
            "//span[text()='Scott']/ancestor::li[@id='p_89/Scott']//input[@type='checkbox']",
        )
        if not find_brand_filter_checkbox.is_selected():
            find_brand_filter_checkbox.click()
        find_brand_filter_checkbox = self.driver.find_element(
            By.XPATH,
            "//span[text()='Scott']/ancestor::li[@id='p_89/Scott']//input[@type='checkbox']",
        )
        is_selected = find_brand_filter_checkbox.is_selected()
        return is_selected

def customer_reviews_filter_selected(self):
        choose_customer_review_filter = self.driver.find_element(
            By.XPATH, "//section[@aria-label='4 Stars & Up']"
        )
        is_selected = choose_customer_review_filter.is_selected()
        return is_selected
"""
