from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
from traceback import print_stack
import utilities.logger as log
import logging


class main_page_header(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    logo_home_menubar="//*[@id='site-header']//div[1]/a/img"
    about_home_menubar="//*[@id='menu-item-2413']"
    services_home_menubar="//*[@id='menu-item-2414']"
    blog_home_menubar="//*[@id='menu-item-1804']"
    case_studies_home_menubar="//*[@id='menu-item-2412']"
    careers_home_menubar="//*[@id='menu-item-2591']"
    contact_home_menubar="//*[@id='menu-item-1756']"
    now_hiring_topbar="//*[@id='site-topbar']//div[1]/a"
    top_bar_text="//*[@id='site-topbar']/div/div/div[1]"

    def logo_home_menubar_click(self):
        self.elementClick(self.logo_home_menubar)

    def about_home_menubar_click(self):
        self.elementClick(self.about_home_menubar)

    def services_home_menubar_click(self):
        self.elementClick(self.services_home_menubar)

    def blog_home_menubar_click(self):
        self.elementClick(self.blog_home_menubar)

    def case_studies_home_menubar_click(self):
        self.elementClick(self.case_studies_home_menubar)

    def careers_home_menubar_click(self):
        self.elementClick(self.careers_home_menubar)

    def contact_home_menubar_click(self):
        self.elementClick(self.contact_home_menubar)

    def now_hiring_topbar_click(self):
        self.elementClick(self.now_hiring_topbar)

    def get_top_bar_text_Text(self):
        self.getText(self.top_bar_text)


    def main_page_browsing(self):
        self.logo_home_menubar_click()
        self.about_home_menubar_click()
        self.services_home_menubar_click()
        self.blog_home_menubar_click()
        self.case_studies_home_menubar_click()
        self.careers_home_menubar_click()
        self.contact_home_menubar_click()
        self.now_hiring_topbar_click()
        self.get_top_bar_text_Text()
