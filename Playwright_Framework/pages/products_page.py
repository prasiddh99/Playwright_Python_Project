from utilities.base_page import BasePage

class ProductsPage(BasePage):

    def open_products(self):
        self.click("a[href='/products']")

    def add_first_product(self):
        self.hover(".product-image-wrapper")
        self.click("a[data-product-id='1']")