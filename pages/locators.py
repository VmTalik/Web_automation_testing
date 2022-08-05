from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[class ='btn btn-lg btn-primary btn-add-to-basket']")
    GOOD_ADDED_MESSAGE = (
        By.CSS_SELECTOR, "div[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1)")
    GOOD_NAME = (By.CSS_SELECTOR, "div[class = 'col-sm-6 product_main']>h1")
    GOOD_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    BASKET_FULL_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p:nth-child(1)")
    BASKET_VALUE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    PRICE_VALUE = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>[class = 'btn btn-default']")
    GOODS_IN_BASKET_HEADER = (By.CSS_SELECTOR, "[class = 'col-sm-6 h3']")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
