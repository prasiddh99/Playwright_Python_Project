from datetime import datetime

class BasePage:

    def __init__(self, page):

        self.page = page

    def click(self, locator):

        self.page.locator(locator).click()

    def fill(self, locator, text):

        self.page.locator(locator).fill(text)

    def hover(self, locator):

        self.page.locator(locator).hover()

    def is_visible(self, locator):

        return self.page.locator(locator).is_visible()

    def select_dropdown(self, locator, value):

        self.page.locator(locator).select_option(value)

    def check_radio(self, locator):

        self.page.locator(locator).check()