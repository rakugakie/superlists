from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):

        #internally resolves urls and find which view function they map to.
        #Were check that resolve, when called with '/', finds a function
        #called home_page
        
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        #Create a httpRequest Object, which django
        #will see when a users browser asks for a page
        
        request = HttpRequest()

        #We pass the request to our homepage, qhich gives it a response.
        #This response is an instance of class HttpResponse
        response = home_page(request)

        #Then, we extract the .content of the request.  We decode it with
        #.decode() to convert them into a string of HTML thats being sent to the user
        html = response.content.decode('utf8')

        
        self.assertTrue(html.startswith('<html>'))

        #We Want a Title of To-Do list, because that's what we specified in
        #our functional test
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
                                      

