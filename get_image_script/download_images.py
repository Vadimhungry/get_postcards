import requests
from urllib.parse import urlparse
import os


def download_images(links, downloads_directory):
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            url_file_name = urlparse(link).path[3:]
            file_name = f'meshok-{url_file_name[0:-7]}-{url_file_name[-6:]}'
            filepath = os.path.join(downloads_directory, file_name)
            # Открыть файл для записи в двоичном режиме
            with open(filepath, "wb") as f:
                # Записать содержимое ответа в файл
                f.write(response.content)
            print(f"{file_name} - изображение скачано!")
        else:
            print(
                "Ошибка при скачивании изображения. Код состояния:",
                response.status_code
            )
