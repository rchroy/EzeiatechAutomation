from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
from traceback import print_stack
import utilities.logger as log
import logging
import time

class main_page_footer(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    accept_all_button="//div[@class='cky-consent-bar']//button[@class='cky-btn cky-btn-accept']"
    it_consulting_footer_link="//div[@class='footer-aside-wrap']//a[@href='/services/it-consulting/']"
    it_support_footer_link="//div[@class='footer-aside-wrap']//a[@href='/services/it-support/']"
    automation_testing_footer_link="//div[@class='footer-aside-wrap']//a[@href='/services/automation-testing/']"
    cloud_computing_footer_link="//li[4]/a[@href='/services/cloud-computing/']"
    managed_it_footer_link="//li[5]/a[@href='/services/managed-it/']"
    about_us_footer_link="//li[1]/a[@href='/about/']"
    careers_footer_link="//li[2]/a[@href='/careers/']"
    blog_footer_link="//li[3]/a[@href='/blog/']"
    contact_us_footer_link="//li[4]/a[@href='/contact-us/']"
    facebook_footer_link="//div[@class='footer-aside-wrap']//ul[@class='sub-menu']//a[@href='https://www.facebook.com/ezeiatech/']"
    twitter_footer_link="//div[@class='footer-aside-wrap']//ul[@class='sub-menu']//a[@href='https://twitter.com/EzeiaTech']"
    linkedin_footer_link="//div[@class='footer-aside-wrap']//a[@href='https://www.linkedin.com/company/ezeiatech-systems-pvt-ltd']"

    def accept_all_btn_click(self):
        self.elementClick(self.accept_all_button)

    def it_consulting_footer_link_click(self):
        self.elementClick(self.it_consulting_footer_link)

    def it_support_footer_link_click(self):
        self.elementClick(self.it_support_footer_link)

    def automation_testing_footer_link_click(self):
        self.elementClick(self.automation_testing_footer_link)

    def cloud_computing_footer_link_click(self):
        self.elementClick(self.cloud_computing_footer_link)

    def managed_it_footer_link_click(self):
        self.elementClick(self.managed_it_footer_link)

    def about_us_footer_link_click(self):
        self.elementClick(self.about_us_footer_link)

    def careers_footer_link_click(self):
        self.elementClick(self.careers_footer_link)

    def blog_footer_link_click(self):
        self.elementClick(self.blog_footer_link)

    def contact_us_footer_link_click(self):
        self.elementClick(self.contact_us_footer_link)

    def facebook_footer_link_click(self):
        self.elementClick(self.facebook_footer_link)

    def twitter_footer_link_click(self):
        self.elementClick(self.twitter_footer_link)

    def linkedin_footer_link_click(self):
        self.elementClick(self.linkedin_footer_link)

    def main_page_footer_browsing(self):
        self.accept_all_btn_click()
        self.it_consulting_footer_link_click()
        self.it_support_footer_link_click()
        self.automation_testing_footer_link_click()
        self.cloud_computing_footer_link_click()
        self.managed_it_footer_link_click()
        self.about_us_footer_link_click()
        self.careers_footer_link_click()
        self.blog_footer_link_click()
        self.contact_us_footer_link_click()
        self.facebook_footer_link_click()
        self.goback()
        self.twitter_footer_link_click()
        self.goback()
        self.goback()
        self.linkedin_footer_link_click()
        self.goback()
