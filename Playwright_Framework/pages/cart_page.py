from utilities.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

    def verify_products_in_cart(self):

        product1 = self.is_visible("#product-1")

        product2 = self.is_visible("#product-2")

        return product1 and product2

    def proceed_to_checkout(self):

        self.click("text=Proceed To Checkout")