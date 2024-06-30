from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
from traceback import print_stack
import utilities.logger as log
import logging
import time

class main_page_links(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    accept_all_button="//div[@class='cky-consent-bar']//button[@class='cky-btn cky-btn-accept']"
    ai_driven_it_consulting="//div[@class='content']//ul//a[@href='/services/it-consulting/']"
    ai_powered_it_support="//div[@class='content']//ul//a[@href='/services/it-support/']"
    innovative_software_development="//div[@class='content']//a[@href='https://ezeiatech.com/ai-development/']"
    cloud_computing_reinvented="//div[@class='content']//a[@href='/services/cloud-computing/']"
    managed_it_with_intelligence="//div[@class='content']//a[@href='/services/managed-it/']"
    find_your_solution="//div[@class='main-content-inner']/div[@class='content']/section[1]/div[2]//a[@href='/services/']"
    join_us_btn="//div[@class='content']//a[@href='/careers/']"
    find_out_more="//section[2]/div[3]//a[@href='/services/']"
    view_case_studies="//div[2]//a[@href='/case-studies/']"
    get_free_consultations_btn="//div[5]/div[@class='row-inner']//a[@href='/contact-us/']"
    contact_us_btn="//div[@class='content-bottom-widgets']//a[@href='/contact-us/']"    

    def accept_all_btn_click(self):
        self.elementClick(self.accept_all_button)

    def ai_driven_it_consulting_click(self):
        self.elementClick(self.ai_driven_it_consulting)

    def ai_powered_it_support_click(self):
        self.elementClick(self.ai_powered_it_support)

    def innovative_software_development_click(self):
        self.elementClick(self.innovative_software_development)

    def cloud_computing_reinvented_click(self):
        self.elementClick(self.cloud_computing_reinvented)

    def managed_it_with_intelligence_click(self):
        self.elementClick(self.managed_it_with_intelligence)

    def find_your_solution_click(self):
        self.elementClick(self.find_your_solution)

    def join_us_btn_click(self):
        self.elementClick(self.join_us_btn)

    def find_out_more_click(self):
        self.elementClick(self.find_out_more)

    def view_case_studies_click(self):
        self.elementClick(self.view_case_studies)

    def get_free_consultations_btn_click(self):
        self.elementClick(self.get_free_consultations_btn)

    def contact_us_btn_click(self):
        self.elementClick(self.contact_us_btn)

    def main_page_links_browsing(self):
        self.accept_all_btn_click()
        self.ai_driven_it_consulting_click()
        self.goback()
        self.ai_powered_it_support_click()
        self.goback()
        self.innovative_software_development_click()
        self.goback()
        self.cloud_computing_reinvented_click()
        self.goback()
        self.managed_it_with_intelligence_click()
        self.goback()
        self.find_your_solution_click()
        self.goback()
        self.join_us_btn_click()
        self.goback()
        self.find_out_more_click()
        self.goback()
        self.view_case_studies_click()
        self.goback()
        self.get_free_consultations_btn_click()
        self.goback()
        self.contact_us_btn_click()
        self.goback()
        
