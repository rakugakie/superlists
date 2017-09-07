from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):

        #internally resolves urls and find which view function they map to.
        #Were check that resolve, when called with '/', finds a function
        #called home_page
        
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        

