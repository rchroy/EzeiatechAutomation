from pages.main_page_sidebar.main_page_sidebar import main_page_sidebar
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class main_page_sidebar_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = main_page_sidebar(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.main_page_sidebar_browsing()