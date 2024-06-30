from pages.main_page_footer.main_page_footer_page import main_page_footer 
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class main_page_footer_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = main_page_footer(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.main_page_footer_browsing()