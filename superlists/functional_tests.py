from selenium import webdriver

browser = webdriver.Firefox()

#Edith goes to new online to-do app
browser.get('htp://localhost:8000')

#She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

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


browser.quit()

