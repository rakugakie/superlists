from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        #Manually call glient.get and pass url we want to test
        response = self.client.get('/')

        #Django test class.
        self.assertTemplateUsed(response, 'home.html')
        
    def test_can_save_a_POST_request(self):
        #Do a post- call self.client.post, includes data which contains data.

        response = self.client.post('/', data={'item_text': 'A new list item'})

        #Check that the text from POST request ends up in rendered HTML.
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


        

