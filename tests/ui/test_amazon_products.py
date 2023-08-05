from modules.ui.page_objects.Amazon_pages.product_listing_page import ProductListingPage
import pytest
import time


# test checks that result info bar contains the same product name as it was used during product search
@pytest.mark.amazon_products
def test_check_product_search_in_header(product_listing_page):
    product_listing_page.search_product("paper towels bulk")
    assert product_listing_page.verify_result_info_bar("paper towels bulk")
    product_listing_page.close()


# test checks that filter option is selected after clicking
@pytest.mark.amazon_products
def test_check_customer_review_filter_selection(product_listing_page):
    product_listing_page.search_product("paper towels bulk")
    product_listing_page.customer_reviews_filter()
    result = product_listing_page.clear_link_option_customer_reviews_filter()
    assert result == True
    product_listing_page.close()


"""
# test checks that Clear link appears after filter option selection
@pytest.mark.amazon_products1
def test_check_brans_filter_selection():
    search = ProductListingPage()
    search.navigate_to()
    search.search_product("paper towels bulk")
    time.sleep(2)
    search.brands_filter_selection()
    time.sleep(2)
    search.clear_link_option_in_brands_filter()
    result = search.clear_link_option_in_brands_filter()
    assert result == True
    search.close()
"""
