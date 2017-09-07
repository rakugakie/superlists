from selenium import webdriver

broswer = webdriver.Firefox()
browser.get('htp://localhost:8000')

assert 'Django' in browser.title
