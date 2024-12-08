# weather-forecast-site

## Описание

Это приложение предоставляет информацию о погоде для заданных городов с использованием API AccuWeather. Пользователи могут вводить названия городов и получать текущие данные о погоде.

## Установка

1. Убедитесь, что у вас установлен Python и pip.
2. Установите необходимые зависимости:

   ```bash
   pip install requests flask
   ```

3. Создайте файл `.env` и добавьте ваш API ключ:

   ```python
   API_KEY = "your_api_key_here"
   DEBUG = True  # Установите False для продакшн-режима
   ```

## Использование

1. Запустите приложение:

   ```bash
   python app.py
   ```

2. Откройте браузер и перейдите по адресу `http://127.0.01:5000`.

3. Введите названия городов и нажмите кнопку для получения данных о погоде.

## Обработка ошибок

Приложение обрабатывает различные ошибки, включая:

- Ошикби ввода данных.
- Ошибки взаимодействия с API.
- Отсутствие данных о местоположении или погоде.

При возникновении ошибки пользователю будет показано соответствующее сообщение.
