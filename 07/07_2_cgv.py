import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

# sect-movie-chart

sect_movie_chart = soup.select_one(".sect-movie-chart")

movie_chart = sect_movie_chart.select("li")

print(len(movie_chart)) # 19개가 나왔으므로 movie_chart 안에서 반복을 돌리며 추출하면 됨

for movie in movie_chart:
    title = movie.select_one(".title")
    score = movie.select_one(".score") # 예매율 %와 선호도 %가 함께 들어 있는 class
    ticketing = score.select_one(".percent")
    print(title.text)
    print(ticketing.text)
    print()