import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        self.visit_homepage()
        self.check_page_title_contains('To-Do')

        self.fail('Finish the test!')

    def visit_homepage(self) -> None:
        self.browser.get('http://localhost:8000')

    def check_page_title_contains(self, search_for) -> None:
        self.assertIn(search_for, self.browser.title)

    # Enter a new to-do item

    # Press Enter

    # New to-do item is visible in to-do list

    # Enter a second to-do item

    # Leave the homepage

    # Visit home page again

    # all the to-do items are still present


if __name__ == '__main__':
    unittest.main(warnings='ignore')
