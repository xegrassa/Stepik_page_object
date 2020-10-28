from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.CSS_SELECTOR, 'span a.btn.btn-default[href="/en-gb/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner a[href="/en-gb/"]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRODUCT_COST = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ADDED_ITEM_TO_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) strong")
    BASKET_COST = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) strong")
