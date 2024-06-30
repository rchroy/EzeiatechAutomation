import unittest
from tests.main_page_header.main_page_header_Test import main_page_header_Tests
from tests.main_page_sidebar.main_page_sidebar_Test import main_page_sidebar_Tests
from tests.main_page_footer.main_page_footer_Test import main_page_footer_Tests
from tests.main_page_links.main_page_links_Test import main_page_links_Tests

tc1 = unittest.TestLoader().loadTestsFromTestCase(main_page_header_Tests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(main_page_sidebar_Tests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(main_page_footer_Tests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(main_page_links_Tests)

smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
