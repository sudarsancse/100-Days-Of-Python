import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res =  requests.get(URL)

res.raise_for_status()
website_html = res.text

soup = BeautifulSoup(website_html, "html.parser")
movies_name = soup.find_all(name="h3", class_="title")
movies_titles = [name.getText() for name in movies_name]

all_movies_name = movies_titles[::-1]

with open("movies.txt", "w",encoding="utf-8") as file:
    for movie_name in all_movies_name:
        file.write(f"{movie_name}\n")