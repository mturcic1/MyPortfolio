from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
anchor_tags = soup.find_all(name="a")

for tag in anchor_tags:
    print(tag.get("href"))

heading = soup.find_all(name="h1", id="name")
print(heading)
section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading[0].text)

company_url = soup.select_one(selector="p a")
print(company_url)