from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET)

    def should_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET)
