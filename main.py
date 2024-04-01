import requests

# Запрашиваем у пользователя URL и API-ключ
url = input("Введите URL: ")
api_key = input("Введите API-ключ: ")

# Формируем заголовки для запроса
headers = {
    "X-API-KEY": api_key,
    "Content-Type": "application/json"
}

# Делаем запрос к API с помощью библиотеки requests
response = requests.get(url, headers=headers)

# проверяем был ли запрос успешным (статус-код 200)
if response.status_code == 200:
    # парсим данные в формате JSON
    data = response.json()
    # выводим даныые о фильме
    print(f"Название фильма: {data['nameRu']}")
    print(f"Описание: {data['description']}")
    print(f"Рейтинг: {data['ratingKinopoisk']}")
    print(f"Год выпуска: {data['year']}")
else:
    # Обрабатываем ошибку в случае неудачного запроса
    print(f"Ошибка: - {response.text}")