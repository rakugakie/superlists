from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.models import Item, List

from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):

        # Manually call client.get and pass url we want to test
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):

        # Create list object
        list_ = List()
        list_.save()

        #Create two item objects
        first_item = Item()
        first_item.text = 'The first ever list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = list_
        second_item.save()

        # assert that the list_ is the first list in DB
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        # assert there are two saved items
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        # assert some shit, including lists
        self.assertEqual(first_saved_item.text, first_item.text)
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, second_item.text)
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemy 1', list=list_)
        Item.objects.create(text='itemy 2', list=list_)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemy 1')
        self.assertContains(response, 'itemy 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        # Post first list item
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # Asserts there is but one item
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # Assertion takes response, expected_url, status code (Default 302),
        # Target status code (default 200), mesage prefix,
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
