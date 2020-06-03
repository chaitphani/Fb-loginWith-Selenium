from selenium import webdriver
#from credentials_all import fb_username, fb_pass


# to login...
fb_username = input('Enter a valid username or mail id: ')

fb_pass = input('Enter a valid password to login: ')

url = 'https://www.facebook.com/'

driver = webdriver.Chrome('F:\Apps\chromedriver.exe')

driver.maximize_window()

driver.get(url)

driver.find_element_by_id('email').send_keys(fb_username)

driver.find_element_by_id('pass').send_keys(fb_pass)

driver.find_element_by_id('loginbutton').click()

