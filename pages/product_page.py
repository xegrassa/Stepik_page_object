from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_bucket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def get_basket_cost(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_COST).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_added_product_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_ITEM_TO_BASKET).text

    def should_cost_basket_and_product_equal(self):
        assert self.get_product_cost() == self.get_basket_cost(), "Цена корзины отличается от цены добавленного продукта"

    def should_name_added_basket_and_product_equal(self):
        assert self.get_product_name() == self.get_added_product_to_basket(), "Имя добавленного продукта другое"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message должно было пропасть"
