from playwright.sync_api import expect
from playwright.sync_api import sync_playwright
import random
import time


def test_e2e_checkout():
    def generate_email():
        return f"parth{random.randint(1000, 9999)}@gmail.com"

    with sync_playwright() as p:

        # browser = p.chromium.launch(headless=False)
        browser = p.firefox.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.goto("https://automationexercise.com/")

        # HOME PAGE VALIDATION
        assert page.locator("img[alt='Website for automation practice']").is_visible()

        # CLICK SIGNUP / LOGIN
        page.click("a[href='/login']")

        # USER REGISTRATION
        email = generate_email()
        page.fill("input[data-qa='signup-name']", "Parth Dharmnathi")
        page.fill("input[data-qa='signup-email']", email)
        page.click("button[data-qa='signup-button']")

        # ACCOUNT INFORMATION
        page.check("#id_gender1")

        page.fill("#password", "Parth@123")

        page.select_option("#days", "10")
        page.select_option("#months", "5")
        page.select_option("#years", "1998")

        page.fill("#first_name", "Parth")
        page.fill("#last_name", "Dharmnathi")
        page.fill("#company", "ABC Company")

        page.fill("#address1", "Rajkot Gujarat")
        page.fill("#address2", "India")
        page.select_option("#country", "India")
        page.fill("#state", "Gujarat")
        page.fill("#city", "Rajkot")
        page.fill("#zipcode", "360001")
        page.fill("#mobile_number", "9999999999")

        # Create Account
        page.click("button[data-qa='create-account']")

        # VERIFY ACCOUNT CREATED
        assert page.locator("text=Account Created!").is_visible()
        page.click("a[data-qa='continue-button']")

        # VERIFY LOGIN
        assert page.locator("text=Logged in as").is_visible()

        # PRODUCTS PAGE
        page.click("a[href='/products']")
        page.wait_for_timeout(2000)

        # ADD PRODUCT TO CART
        # page.hover(".product-image-wrapper")
        page.locator(".product-image-wrapper").first.hover()
        page.click("a[data-product-id='1']")
        # Continue Shopping Popup
        page.click("button.btn.btn-success.close-modal.btn-block")

        # Add Second Product
        # page.hover("(//div[@class='product-image-wrapper'])[2]")
        page.locator("(//div[@class='product-image-wrapper'])[2]").hover()
        page.click("a[data-product-id='2']")

        # View Cart
        page.click("text=View Cart")

        # VERIFY PRODUCTS IN CART
        assert page.locator("#product-1").is_visible()
        assert page.locator("#product-2").is_visible()
        # PROCEED TO CHECKOUT
        page.click("text=Proceed To Checkout")

        # VERIFY ADDRESS DETAILS
        expect(page.locator("#address_delivery")).to_be_visible()

        # PLACE ORDER
        page.fill("textarea[name='message']", "Please deliver quickly")
        page.click("a[href='/payment']")

        # PAYMENT DETAILS
        page.fill("input[name='name_on_card']", "Parth Dharmnathi")
        page.fill("input[name='card_number']", "4111111111111111")
        page.fill("input[name='cvc']", "123")
        page.fill("input[name='expiry_month']", "12")
        page.fill("input[name='expiry_year']", "2030")

        # Pay and Confirm Order
        page.click("#submit")

        # VERIFY ORDER SUCCESS
        assert page.locator("text=Congratulations! Your order has been confirmed!").is_visible()

        print("Test Passed Successfully")

        # Wait before closing
        time.sleep(5)
        browser.close()
