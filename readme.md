# Космический Телеграм

Скрипт скачивает фотографии с сайта NASA и SpaceX. И публикует скачанные фото в случайном порядке в 
Telegram канал с установленной периодичностью

**Набор скриптов**

- скачивает фото с запусков SpaceX
- скачивает APOD-фото от NASA
- скачивает EPIC-фото от NASA
- публикует случайное фото в канал
- вспомогательный скрипт

### Как установить

Для работы необходим установленный python3
1. Скачать архив и распаковать.

2. Получить токен сервиса NASA https://api.nasa.gov/
3. Зарегистрировать телеграм бота https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html
4. Создать канал, получить его id
5. Файл .env.example переименовать в .env, в `NASA_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` 
подставить полученные токены
 ```
   NASA_TOKEN = wEsQfdssgSDFsdSFHFGHE3GHJgJGdf2aeNWX93zd
   TELEGRAM_BOT_TOKEN = 5456552343:AAF_zzxrXC_0LWm9W_ASDFxcvSFASsasVSs
   TELEGRAM_CHAT_ID='-1346423677443'
   ```

6. Установить виртуальное окружение и установить зависимости
```
pip -m venv venv
```
```
pip install -r requirements.txt
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Использование 
### `python fetch_nasa_epic_images.py`
Предназначен для скачивания эпичных фото NASA. Требуется `NASA_TOKEN`

### `python fetch_nasa_apod_images.py`
Предназначен для скачивания фото дня NASA. Требуется `NASA_TOKEN`

### `python fetch_spacex_images.py`
Предназначен для скачивания фото с последнего запуска SpaceX.

При указании id запуска формата `5eb87d47ffd86e000604b38a` скачиваются фото соответствующего запуска

`python fetch_spacex_images.py -i 5eb87d47ffd86e000604b38a`

### `python main.py`
Публикует случайное фото из ранее скачанных в телеграм канал. Требуется `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
По умолчанию период публикации 4 ч (14400 с).
Для установки другого периода необходимо использовать ключ `-d` (значение в секундах)

`python main.py -d 3600` публикация фото раз в 1 час


### Цель проекта ##

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).