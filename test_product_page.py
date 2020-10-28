import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.step13
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "Zvce14f5hj")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_bucket()
        page.solve_quiz_and_get_code()
        page.should_cost_basket_and_product_equal()
        page.should_name_added_basket_and_product_equal()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_is_empty()
    basket_page.should_text_about_empty_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_bucket()
    page.should_disappeared_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_bucket()
    page.should_not_be_success_message()
