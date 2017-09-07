from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        #Manually call glient.get and pass url we want to test
        response = self.client.get('/')

        #Django test class.
        self.assertTemplateUsed(response, 'home.html')                              

