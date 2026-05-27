from utilities.base_page import BasePage
from utilities.test_data import USER_DATA


class AccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def fill_account_information(self):
        self.check_radio("#id_gender1")

        self.fill("#password", USER_DATA["password"])

        self.select_dropdown("#days", "10")
        self.select_dropdown("#months", "5")
        self.select_dropdown("#years", "1998")

        self.fill("#first_name", USER_DATA["first_name"])
        self.fill("#last_name", USER_DATA["last_name"])
        self.fill("#company", USER_DATA["company"])
        self.fill("#address1", USER_DATA["address1"])
        self.fill("#address2", USER_DATA["address2"])

        self.select_dropdown("#country", USER_DATA["country"])

        self.fill("#state", USER_DATA["state"])
        self.fill("#city", USER_DATA["city"])
        self.fill("#zipcode", USER_DATA["zipcode"])
        self.fill("#mobile_number", USER_DATA["mobile_number"])

    def create_account(self):
        self.click("button[data-qa='create-account']")

    def verify_account_created(self):

        # return self.is_visible("text=Account Created!")
        # return self.is_visible("h2[data-qa='account-created']")
        # return self.page.locator("h2.title.text-center b").is_visible()
        locator = self.page.locator("h2.title.text-center b")
        locator.wait_for(state="visible")
        return locator.is_visible()

    def click_continue(self):
        self.click("a[data-qa='continue-button']")

    def verify_logged_in(self):
        return self.is_visible("text=Logged in as")
