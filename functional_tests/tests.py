from django.test import LiveServerTestCase
from django.conf import settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def __init__(self, *args, **kwargs):
        super(NewVisitorTest, self).__init__(*args, **kwargs)
        if settings.DEBUG == False:
            settings.DEBUG = True
            
    
    #Special method that happends before test are run
    def setUp(self):
        self.browser = webdriver.Firefox()
        print("settingup")
        
    #Special Method that happens after tests are run,
    #will run even if error in test
    def tearDown(self):
        self.browser.quit()
        print("tearingdown")
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                   if time.time() - start_time > MAX_WAIT:
                       raise e
                   time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):

        # Edith goes to new online to-do app
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She enters a to-do Item Straight Away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        
        # When she hits enter, the page updates, and now the page lists
        # "!: Buy peacock feathers" As an Item in a to=do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box to add another item.  She adds "Make fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()
        #Now a new user, Francis, comes along to the site.
        #Francis visits the homepage.  No sign of Edith's list
        ##We use a new browser sesssion to make sure no information
        ###from Edith's list is coming through from cookies ect


        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        #He mumbles something about cows and starts his list

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        #Francis gets his own URL
        francist_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, her list is seriously not there lol
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #Satisfied, they sleep, perhaps for the last time in their elderly lives
        
if __name__== '__main__':
    unittest.main(warnings='ignore')

