from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


wiki_statistics_xpath = '//*[@id="articlecount"]/a[1]'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url='http://secure-retreat-92358.herokuapp.com/')

first_name = 'Erik'
last_name = 'Degen'
email = 'erik.degen@yourmom.com'

name_field = driver.find_element(By.NAME, value='fName')
name_field.click()
name_field.send_keys(first_name)

surname_field = driver.find_element(By.NAME, value='lName')
surname_field.click()
surname_field.send_keys(last_name)

email_field = driver.find_element(By.NAME, value='email')
email_field.click()
email_field.send_keys(email)

button_element = driver.find_element(By.XPATH, value='/html/body/form/button')
button_element.click()
