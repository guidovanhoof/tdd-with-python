from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

NEW_ITEM_TEXT = 'Buy peacock feathers'
ANOTHER_NEW_ITEM = 'Use peacock feathers to make a fly'
PLACE_HOLDER = 'Enter a to-do item'
TO_DO = "To-Do"


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        self.visit_homepage()
        self.check_page_title_contains(TO_DO)
        self.check_header_contains(TO_DO)
        self.check_placeholder_contains(PLACE_HOLDER)
        self.enter_new_item(NEW_ITEM_TEXT)
        self.press_enter()
        self.check_list_url()
        self.check_item_present(NEW_ITEM_TEXT)
        self.enter_new_item(ANOTHER_NEW_ITEM)
        self.press_enter()
        self.check_item_present(NEW_ITEM_TEXT)
        self.check_item_present(ANOTHER_NEW_ITEM)
        self.browser.quit()

        self.browser = webdriver.chrome

        self.visit_homepage()
        self.check_item_not_present(NEW_ITEM_TEXT)
        self.check_item_not_present(ANOTHER_NEW_ITEM)
        self.enter_new_item('Buy milk')
        self.press_enter()
        self.check_list_url()
        self.check_item_not_present(NEW_ITEM_TEXT)
        self.check_item_not_present(ANOTHER_NEW_ITEM)

        self.fail('Finish the test!')

    def visit_homepage(self) -> None:
        self.browser.get(self.live_server_url)

    def check_page_title_contains(self, search_text) -> None:
        self.assertIn(search_text, self.browser.title)

    def check_header_contains(self, search_text) -> None:
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn(search_text, header_text)

    def check_placeholder_contains(self, search_text) -> None:
        placeholder = self.get_input_box().get_attribute('placeholder')
        self.assertEqual(placeholder, search_text)

    def get_input_box(self):
        return self.browser.find_element(By.ID, 'new-item')

    def enter_new_item(self, new_item_text):
        self.get_input_box().send_keys(new_item_text)

    def press_enter(self):
        self.get_input_box().send_keys(Keys.ENTER)

    def check_list_url(self):
        list_url = self.browser.current_url
        self.assertRegex(list_url, '/lists/.+')

    def check_item_present(self, item_text):
        todos = self.get_todos()
        self.assertIn(item_text, [todo.text for todo in todos])
        # self.assertTrue(
        #     any(todo.text == item_text for todo in todos),
        #     f'to-do item "{item_text}" not present!'
        # )

    def check_item_not_present(self, item_text):
        todos = self.get_todos()
        self.assertNotIn(item_text, [todo.text for todo in todos])

    def get_todos(self):
        todos = self.browser.find_element(By.ID, 'todos-table')
        return todos.find_elements(By.TAG_NAME, 'tr')

