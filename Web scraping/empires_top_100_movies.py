from bs4 import BeautifulSoup
import requests

# Getting the HTML
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_online_page = response.text
soup = BeautifulSoup(empire_online_page, "html.parser")
dirty_titles = soup.find_all(name="h3", class_="title")
clean_titles = [" ".join(title.text.split()[1:]) for title in dirty_titles]
with open("top_movies.txt", "w", encoding="utf-8") as file:
    for i in range(0, len(clean_titles)):
        file.write(f"{i+1}) {clean_titles[99-i]}\n")

print(clean_titles)