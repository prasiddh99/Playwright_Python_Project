from utilities.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

    def open_signup_login(self):

        self.click("a[href='/login']")

    def signup(self, name, email):

        self.fill("input[data-qa='signup-name']", name)

        self.fill("input[data-qa='signup-email']", email)

        self.click("button[data-qa='signup-button']")