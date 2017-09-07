from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    #Special method that happends before test are run
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    #Special Method that happens after tests are run,
    #will run even if error in test
    def tearDown(self):
        self.browser.quit()

    #Any method whos name starts with test is a test method
    #and will be run by the test runner.
    def test_can_start_a_list_and_retrieve_it_later(self):

        #Edith goes to new online to-do app
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        #She enters a to-do Item Straight Away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        #She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        
        #When she hits enter, the page updates, and now the page lists
        #"!: Buy peacock feathers" As an Item in a to=do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #returns element
        table = self.browser.find_element_by_id('id_list_table')
        #returns list of elements
        #f-statements: Prepend a string with an f, and then use the curly bracked syntax
        #to insert local variables.
        rows = table.find_elements_by_tag_name('tr')
        
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        #There is still a text box to add another item.  She adds "Make fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #The page updates again, and shows both items.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        
        #Edith wonders whether the site will remember he list.
        #She sees that the site had generated a unique URL for her
        #There is some explanatory text to that effect
        self.fail("Finish the test!")
        #She visits that URL, her to do list is still there

        #Satisfied, she goes back to sleep


if __name__== '__main__':
    unittest.main(warnings='ignore')

