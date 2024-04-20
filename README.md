# Скрипт get_postcards

Программа представляет собой CLI - утилиту для терминала.
При запуске программа проанализирует html код со страницы сайта meshok.net и скачает файлы с изображением лицевой и обратной сторон открытки.

## Установка

Для установки выполните команды в терминале:
1. `git clone git@github.com:Vadimhungry/get_postcards.git`
2. `pip install poetry`
3. `python3 -m pip install --user dist/*.whl`

## Использование

Команда `get-postcards get_image_script/fixture/Открытое_письмо_Мешок.html get_image_script/downloaded_postcards` запускает скрипт.

По ней будет проанализирован файл в каталоге программы `get_image_script/fixture/Открытое_письмо_Мешок.html`.

Картинки скачаются в директорию `get_image_script/downloaded_postcards`.

Можно указать программе другие пути.