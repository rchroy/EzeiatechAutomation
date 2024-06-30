from pages.main_page_header.main_page_header_page import main_page_header 
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class main_page_header_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = main_page_header(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.main_page_browsing()