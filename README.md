# News API Service

Простой REST API сервис для работы с новостями и комментариями.

## Установка и запуск

1. Склонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Запустите сервис:
```bash
python main.py
```
Сервис будет доступен по адресу: `http://localhost:8080`

## API Endpoints

### GET /
Получение списка активных новостей

**Response:**
```json
{
    "news": [
        {
            "id": 101,
            "title": "News Title",
            "date": "2023-12-01T10:00:00",
            "body": "News content",
            "deleted": false,
            "comments_count": 2
        }
    ],
    "news_count": 1
}
```

### GET /news/{news_id}
Получение конкретной новости по ID

**Response:**
- Успешный (200):
```json
{
    "id": 101,
    "title": "News Title",
    "date": "2023-12-01T10:00:00",
    "body": "News content",
    "deleted": false,
    "comments": [
        {
            "id": 201,
            "title": "Comment Title",
            "comment": "Comment text"
        }
    ],
    "comments_count": 1
}
```
- Ошибка (404): `News not found`

## Тестирование

Для запуска тестов используйте команду:
```bash
pytest --disable-warnings -v
```

Тесты проверяют:
- Получение списка активных новостей
- Получение существующей новости по ID
- Получение удаленной новости (404)
- Получение несуществующей новости (404)