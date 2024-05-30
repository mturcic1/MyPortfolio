from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# GLOBALS
USERNAME = 'FixYourGameTodd' # enter your username and password here
PASSWORD = 'Naglonakrumpir3'
UPLOAD_SPEED_CONTRACT_VALUE = 100 # enter your contract speed here
DOWNLOAD_SPEED_CONTRACT_VALUE = 100

message_to_internet_provider = """
Dear @TMobileHelp,

Paying for "high-speed" internet but getting dial-up nostalgia is quite the experience. Your service is as reliable as a paper umbrella in a hurricane. Could you please upgrade me to the 21st century? Thanks ever so much.

Warmest regards,
All users

"""

# get internet speed
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.speedtest.net/')

try:
    reject_cookies_button_element = driver.find_element(By.ID, value='onetrust-reject-all-handler')
    reject_cookies_button_element.click()
except Exception as e:
    pass
finally:
    pass

go_button_element = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button_element.click()
sleep(60)

download_speed_element_text = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
upload_speed_element_text = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
driver.quit()

current_upload_speed = float(upload_speed_element_text)
current_download_speed = float(download_speed_element_text)



#  Twitter login
if current_download_speed < DOWNLOAD_SPEED_CONTRACT_VALUE or current_upload_speed < UPLOAD_SPEED_CONTRACT_VALUE:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://x.com/i/flow/login')
    sleep(5)

    username_bar_element = driver.find_element(By.NAME, value='text')
    username_bar_element.send_keys(USERNAME)
    sleep(1)

    login_next_button_element = driver.find_element(By.XPATH, value="//span[text()='Next']")
    login_next_button_element.click()
    sleep(1)

    password_bar_element = driver.find_element(By.NAME, value='password')
    password_bar_element.send_keys(PASSWORD)


    login_final_button_element = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
    login_final_button_element.click()
    sleep(5)

    # You should be now located on front page and below is the tweet to @TMobileHelp 
    refuse_cookies_element = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]') 
    refuse_cookies_element.click()
    tweet_bar_element = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    tweet_bar_element.send_keys(message_to_internet_provider)

    #tweet_button_element = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    #driver.quit()


