from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from bs4 import BeautifulSoup

# variables used in completing google form
goole_form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdttybksw2ACDsIBNOP8DzplyXX28PLezfJrvznLFcsYiysyA/viewform?usp=sf_link' # google form link, can be replaced by any form with 3 questions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class realEstateScrapper:

    @staticmethod
    def get_site_html():
        zillow_site_url = 'https://appbrewery.github.io/Zillow-Clone/'
        response = requests.get(zillow_site_url)
        website_html = response.text
        soup = BeautifulSoup(website_html, "html.parser")
        all_property_addresses = soup.find_all('address', {'data-test': 'property-card-addr'})
        all_property_addresses = [address.text.strip() for address in all_property_addresses]

        all_property_prices = soup.find_all('span', {'class': 'PropertyCardWrapper__StyledPriceLine', 'data-test': 'property-card-price'})
        all_property_prices = [price.text.strip().replace('/mo', '').replace('1 bd', '').strip() for price in all_property_prices]

        all_property_links = soup.find_all('a', {'class': 'StyledPropertyCardDataArea-anchor', 'data-test': 'property-card-link'})
        all_property_links = [link.get('href') for link in all_property_links]
        return all_property_addresses, all_property_prices, all_property_links
    
all_property_addresses, all_property_prices, all_property_links = realEstateScrapper.get_site_html()




def single_entry(address, price, link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(goole_form_link)
    sleep(1)
    
    property_address_element = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address_element.send_keys(address)
    
    property_price_element = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price_element.send_keys(price)
    
    property_link_element = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    property_link_element.send_keys(link)

    send_form_element = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send_form_element.click()

    driver.quit()


for i in range(0, len(all_property_addresses)):
    single_entry(all_property_addresses[i], all_property_prices[i], all_property_links[i])

