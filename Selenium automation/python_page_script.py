from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


upcoming_events_path = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'

upcoming_events = driver.find_element(By.XPATH, value=upcoming_events_path).text
upcoming_events = upcoming_events.split('\n')

upcoming_events_times = [upcoming_events[i] for i in range(0, len(upcoming_events), 2)]
upcoming_event_names = [upcoming_events[i + 1] for i in range(0, (len(upcoming_events) -1), 2)]

print(upcoming_event_names)
print(upcoming_events_times)

upcoming_events = {i: {upcoming_event_names[i]: upcoming_events_times[i]} for i in range(0, len(upcoming_events_times))}

print(upcoming_events)



driver.quit()