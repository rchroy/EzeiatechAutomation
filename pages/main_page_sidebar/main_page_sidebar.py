from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
from traceback import print_stack
import utilities.logger as log
import logging


class main_page_sidebar(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    home_sidebar_menu="//*[@id='menu-item-1796']"
    about_sidebar_menu="//*[@id='menu-item-1797']"
    about_sub_menu_sidebar='//*[@id="menu-item-2178"]'
    careers_sub_menu_sidebar='//*[@id="menu-item-2174"]'
    contact_us_sub_menu_sidebar='//*[@id="menu-item-2176"]'
    services_sidebar_menu="//*[@id='menu-item-1795']"
    it_consulting_sub_menu_sidebar='//*[@id="menu-item-2173"]'
    it_support_sub_menu_sidebar='//*[@id="menu-item-751"]'
    automation_testing_sub_menu_sidebar='//*[@id="menu-item-747"]'
    cloud_computing_sub_menu_sidebar='//*[@id="menu-item-748"]'
    managed_it_sub_menu_sidebar='//*[@id="menu-item-750"]'
    zoho_development_sub_menu_sidebar='//*[@id="menu-item-3010"]'
    web_30_sub_menu_sidebar='//*[@id="menu-item-3356"]'
    all_services_sub_menu_sidebar='//*[@id="menu-item-1793"]'
    blog_sidebar_menu="//*[@id='menu-item-2183']"
    case_studies_sidebar_menu="//*[@id='menu-item-1798']"
    
    def home_sidebar_menu_click(self):
        self.elementClick(self.home_sidebar_menu)

    def about_sidebar_menu_click(self):
        self.elementClick(self.about_sidebar_menu)

    def about_sub_menu_sidebar_click(self):
        self.elementClick(self.about_sub_menu_sidebar)

    def careers_sub_menu_sidebar_click(self):
        self.elementClick(self.careers_sub_menu_sidebar)

    def contact_us_sub_menu_sidebar_click(self):
        self.elementClick(self.contact_us_sub_menu_sidebar)

    def services_sidebar_menu_click(self):
        self.elementClick(self.services_sidebar_menu)

    def it_consulting_sub_menu_sidebar_click(self):
        self.elementClick(self.it_consulting_sub_menu_sidebar)

    def it_support_sub_menu_sidebar_click(self):
        self.elementClick(self.it_support_sub_menu_sidebar)

    def automation_testing_sub_menu_sidebar_click(self):
        self.elementClick(self.automation_testing_sub_menu_sidebar)

    def cloud_computing_sub_menu_sidebar_click(self):
        self.elementClick(self.cloud_computing_sub_menu_sidebar)

    def managed_it_sub_menu_sidebar_click(self):
        self.elementClick(self.managed_it_sub_menu_sidebar)

    def zoho_development_sub_menu_sidebar_click(self):
        self.elementClick(self.zoho_development_sub_menu_sidebar)

    def web_30_sub_menu_sidebar_click(self):
        self.elementClick(self.web_30_sub_menu_sidebar)

    def all_services_sub_menu_sidebar_click(self):
        self.elementClick(self.all_services_sub_menu_sidebar)

    def blog_sidebar_menu_click(self):
        self.elementClick(self.blog_sidebar_menu)

    def case_studies_sidebar_menu_click(self):
        self.elementClick(self.case_studies_sidebar_menu)

    def main_page_sidebar_browsing(self):
        self.home_sidebar_menu_click()
        self.about_sidebar_menu_click()
        self.careers_sub_menu_sidebar_click()
        self.about_sidebar_menu_click()
        self.contact_us_sub_menu_sidebar_click()
        self.about_sidebar_menu_click()
        self.services_sidebar_menu_click()
        self.it_consulting_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.it_support_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.automation_testing_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.cloud_computing_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.managed_it_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.zoho_development_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.web_30_sub_menu_sidebar_click()
        self.services_sidebar_menu_click()
        self.all_services_sub_menu_sidebar_click()
        self.blog_sidebar_menu_click()
        self.case_studies_sidebar_menu_click()

