from pages.main_page_links.main_page_links_page import main_page_links 
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class main_page_links_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = main_page_links(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.main_page_links_browsing()