from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from lists.models import TodoItem
from lists.views import home_page
from utils.html import remove_csfr


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = home_page(request)

        expected_html = render_to_string('lists/home_page.html', request=request)
        self.assertEqual(
            remove_csfr(response.content.decode()),
            remove_csfr(expected_html),
            'html for home page not correct!'
        )

    def test_home_page_can_save_a_post_request(self):
        new_item = 'A new todo-item'
        request = HttpRequest()
        request.method = 'POST'
        request.POST['new-item'] = new_item

        response = home_page(request)

        self.assertIn(new_item, response.content.decode())
        expected_html = render_to_string(
            'lists/home_page.html',
            {'new_item': new_item}
        )
        self.assertEqual(
            remove_csfr(response.content.decode()),
            remove_csfr(expected_html)
        )


class TodoItemModelTest(TestCase):
    def test_saving_and_retrieving_todo_items(self):
        first_item = TodoItem()
        first_item.text = 'The first (ever) todo item'
        first_item.save()

        second_item = TodoItem()
        second_item.text = 'The second todo item'
        second_item.save()

        saved_items = TodoItem.objects.all()

        self.assertEqual(saved_items.count(), 2)
        self.assertIn(first_item, saved_items)
        self.assertIn(second_item, saved_items)

