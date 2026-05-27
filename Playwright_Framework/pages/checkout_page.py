from utilities.base_page import BasePage
from Playwright_Framework.utilities.test_data import PAYMENT_DATA


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def verify_address_details(self):
        return self.is_visible("#address_delivery")

    def place_order(self):
        self.fill(
            "textarea[name='message']",
            "Please deliver quickly"
        )

        self.click("a[href='/payment']")

    def enter_payment_details(self):
        self.fill(
            "input[name='name_on_card']",
            PAYMENT_DATA["name_on_card"]
        )

        self.fill(
            "input[name='card_number']",
            PAYMENT_DATA["card_number"]
        )

        self.fill(
            "input[name='cvc']",
            PAYMENT_DATA["cvc"]
        )

        self.fill(
            "input[name='expiry_month']",
            PAYMENT_DATA["expiry_month"]
        )

        self.fill(
            "input[name='expiry_year']",
            PAYMENT_DATA["expiry_year"]
        )

    def confirm_order(self):
        self.click("#submit")

    def verify_order_success(self):
        locator = self.page.locator("text=Order Placed!")
        locator.wait_for(state="visible")
        return locator.is_visible()
