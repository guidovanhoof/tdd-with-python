from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from lists.models import TodoItem, List
from lists.views import home_page
from utils.html import remove_csfr

ITEM = 'A new todo-item'


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


class TodoItemAndListModelTest(TestCase):
    def test_saving_and_retrieving_todo_items(self):
        list_ = List()
        list_.save()

        first_item = TodoItem()
        first_item.text = 'The first (ever) todo item'
        first_item.list = list_
        first_item.save()

        second_item = TodoItem()
        second_item.text = 'The second todo item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = TodoItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertIn(first_item, saved_items)
        self.assertEqual(first_item.list, list_)
        self.assertIn(second_item, saved_items)
        self.assertEqual(second_item.list, list_)


class ListViewTest(TestCase):
    def test_displays_all_items_for_a_list(self):
        todo_list = List.objects.create()
        TodoItem.objects.create(text='to-do item 1', list=todo_list)
        TodoItem.objects.create(text='to-do item 2', list=todo_list)
        other_todo_list = List.objects.create()
        TodoItem.objects.create(text='other to-do item 1', list=other_todo_list)
        TodoItem.objects.create(text='other to-do item 2', list=other_todo_list)

        response = self.client.get(f'/lists/{todo_list.id}/')

        self.assertContains(response, 'to-do item 1')
        self.assertContains(response, 'to-do item 2')
        self.assertNotContains(response, 'other to-do item 1')
        self.assertNotContains(response, 'other to-do item 2')

    def test_uses_list_template(self):
        todo_list = List.objects.create()

        response = self.client.get(f'/lists/{todo_list.id}/')

        self.assertTemplateUsed(response, 'lists/list.html')


class NewListTest(TestCase):
    def test_can_save_a_post_request(self):
        self.client.post(
            '/lists/new/',
            data={
                'new-item': ITEM,
            }
        )

        self.assertEqual(TodoItem.objects.count(), 1)
        todo_item = TodoItem.objects.first()
        self.assertEqual(todo_item.text, ITEM)

    def test_redirects_after_post(self):
        response = self.client.post(
            '/lists/new/',
            data={
                'new-item': ITEM,
            }
        )

        todo_list = List.objects.first()
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response, f'/lists/{todo_list.id}/')
