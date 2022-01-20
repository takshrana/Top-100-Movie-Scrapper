import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
em_website = response.text

soup = BeautifulSoup(em_website, "html.parser")
titles = soup.find_all(name="h3")
print(titles)
# movie_list = []
# for movie in titles:
#     movie_list.append(movie.getText())
#
# print(movie_list)