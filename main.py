from urllib.request import urlopen
from bs4 import BeautifulSoup

# очищаем код от выбранных элементов
def delete_div(code, tag, arg):
    # находим все указанные теги с параметрами
    for div in code.find_all(tag, arg):
        # и удаляем их из кода
        div.decompose()


# получаем исходный код страницы
inner_html_code = str(urlopen('https://thecode.media/parsing-2/').read(), 'utf-8')

# отправляем исходный код страницы на обработку в библиотеку
inner_soup = BeautifulSoup(inner_html_code, "html.parser")

title = inner_soup.find('title').text

# Только блок с содержанием статьи
inner_soup = inner_soup.find('div', {"class": 'article-content'})

# удаляем титры
delete_div(inner_soup, "div", {'class': "wp-block-lazyblock-titry"})

# удаляем все возможные баннеры (код баннеров от 1 до 99)
for i in range(99):
    delete_div(inner_soup, "div", {'class': "wp-block-lazyblock-banner" + str(i)})

# Удаляем боковые ссылки
delete_div(inner_soup, "div", {'class': "wp-block-lazyblock-link-aside"})

# удаляем кат
delete_div(inner_soup, "div", {"class": "accordion"})

# удаляем преформатированный код
delete_div(inner_soup, 'pre', '')

# удаляем вставки с кодом
delete_div(inner_soup, 'code', '')

print(title)
print(inner_soup.get_text())
