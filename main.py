from urllib.request import urlopen
from bs4 import BeautifulSoup

# получаем исходный код страницы
inner_html_code = str(urlopen('https://thecode.media/parsing-2/').read(), 'utf-8')
# отправляем исходный код страницы на обработку в библиотеку
inner_soup = BeautifulSoup(inner_html_code, "html.parser")

print(inner_soup.get_text())
