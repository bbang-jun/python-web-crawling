from bs4 import BeautifulSoup

html = "<a class=\"logo_naver\">네이버 구글 다음<span class = \"blind\">네이버</span></a>"

soup = BeautifulSoup(html, "html.parser")

logo = soup.select_one(".logo_naver")

print(f"text : {logo.text}")
print(f"string : {logo.string}")

# .text와 .string의 차이점