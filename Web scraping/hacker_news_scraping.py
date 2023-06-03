from bs4 import BeautifulSoup
import requests

# Getting the HTML
response = requests.get(url="https://news.ycombinator.com/")
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")
article_tags = soup.find_all(class_="titleline")

# Create lists for titles, articles and upvote points
article_texts = []
article_links = []
for tag in article_tags:
    article_text = tag.get_text()
    article_link = tag.find("a").get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

point_list = [int(item.text[1:4].strip()) if str(item.text[1:4].strip()).isdigit() else 0 for item in
              soup.find_all(class_="subtext")]

# Locate index of the maximum value
max_value = 0
for i in range(0, len(point_list)):
    if point_list[i] > max_value:
        max_value = point_list[i]
top_index = point_list.index(max_value)

print(
    f"Top rated article is '{article_texts[top_index]}' with {max_value} upvotes and you can find article at {article_links[top_index]}.")
