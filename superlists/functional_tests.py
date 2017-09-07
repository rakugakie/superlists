from selenium import webdriver
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
        
        #Fails the test automatically
        self.fail('Finish the test')

        #She enters a to-do Item Straight Away

        #She types "Buy peacock feathers" into a text box

        #When she hits enter, the page updates, and now the page lists
        #"!: Buy peacock feathers" As an Item in a to=do list

        #There is still a text box to add another item.  She adds "Make fly"

        #The page updates again, and shows both items.

        #Edith wonders whether the site will remember he list.
        #She sees that the site had generated a unique URL for her
        #There is some explanatory text to that effect

        #She visits that URL, her to do list is still there

        #Satisfied, she goes back to sleep


if __name__== '__main__':
    unittest.main(warnings='ignore')

