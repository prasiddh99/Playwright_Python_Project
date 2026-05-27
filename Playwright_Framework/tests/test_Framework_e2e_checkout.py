from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utilities.helpers import generate_random_email
from Playwright_Framework.utilities.test_data import USER_DATA


def test_e2e_checkout(page):
    login = LoginPage(page)

    account = AccountPage(page)

    home = HomePage(page)

    cart = CartPage(page)

    checkout = CheckoutPage(page)

    # VERIFY HOME PAGE
    assert home.verify_home_page_loaded()

    # OPEN LOGIN PAGE
    login.open_signup_login()

    # SIGNUP
    email = generate_random_email()

    login.signup(USER_DATA["name"], email)

    # ACCOUNT DETAILS
    account.fill_account_information()

    account.create_account()

    # VERIFY ACCOUNT CREATED
    assert account.verify_account_created()

    account.click_continue()

    # VERIFY LOGIN
    assert account.verify_logged_in()

    # PRODUCTS PAGE
    home.open_products_page()

    # ADD PRODUCTS
    home.add_product_to_cart(1)

    home.continue_shopping()

    home.add_product_to_cart(2)

    # VIEW CART
    home.view_cart()

    # VERIFY PRODUCTS
    assert cart.verify_products_in_cart()

    # CHECKOUT
    cart.proceed_to_checkout()

    # VERIFY ADDRESS
    assert checkout.verify_address_details()

    # PLACE ORDER
    checkout.place_order()

    # PAYMENT
    checkout.enter_payment_details()

    # CONFIRM ORDER
    checkout.confirm_order()

    # VERIFY SUCCESS
    assert checkout.verify_order_success()

    print("Test Passed Successfully")
