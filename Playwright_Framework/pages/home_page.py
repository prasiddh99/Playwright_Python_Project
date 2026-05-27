from utilities.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):

        super().__init__(page)

    def verify_home_page_loaded(self):

        return self.is_visible(
            "img[alt='Website for automation practice']"
        )

    def open_products_page(self):

        self.click("a[href='/products']")

    def add_product_to_cart(self, product_id):
        product = self.page.locator(".product-image-wrapper").nth(product_id - 1)
        product.hover()
        self.page.locator(f"a[data-product-id='{product_id}']").first.click()

    def continue_shopping(self):

        self.click(
            "button.btn.btn-success.close-modal.btn-block"
        )

    def view_cart(self):

        self.click("text=View Cart")