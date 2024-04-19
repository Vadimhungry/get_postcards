from bs4 import BeautifulSoup
import re


def get_img_links(path):

    with open(path) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    # Находим теги с картинками в разделе основного содержания страницы
    div_body_content = soup.find('div', class_='bodyContent_2f94e')
    img_tags = div_body_content.find_all('img')

    # Получаем содержание srcset
    img_srcsets = []
    for tag in img_tags:
        if tag.has_attr('srcset'):
            img_srcsets.append(tag['srcset'])

    # получаем адреса превью картинок
    full_view_urls = []
    pattern = r', (https:\/\/.*?\.jpg) 2x'
    for src in img_srcsets:
        src_url = re.findall(pattern, src)[0]

        correct_url = src_url[:8] + 'b.' + src_url[8:-11] + 'jpeg'
        full_view_urls.append(correct_url)
    return full_view_urls
