import pytest
from aiohttp import web
from app.routes import routes
import sys
import asyncio


@pytest.fixture(scope="session")
def event_loop():
    """
    Фикстура для настройки event loop.
    Для Windows устанавливает специальную политику WindowsSelectorEventLoopPolicy.
    Создает и возвращает новый event loop для всей тестовой сессии.
    """
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_data():
    """
    Фикстура для создания тестовых данных.
    Возвращает кортеж (news_data, comments_data) с моковыми данными для тестов.
    """
    news_data = {
        "news": [
            {
                "id": 101,
                "title": "mock_news_1",
                "date": "2023-12-01T10:00:00",
                "body": "Mocked news 1",
                "deleted": False,
            },
            {
                "id": 102,
                "title": "mock_news_2",
                "date": "2023-12-02T12:00:00",
                "body": "Mocked news 2",
                "deleted": True,
            },
            {
                "id": 103,
                "title": "mock_news_3",
                "date": "2023-12-03T15:00:00",
                "body": "Mocked news 3",
                "deleted": False,
            },
        ],
        "news_count": 3,
    }
    comments_data = {
        "comments": [
            {
                "id": 201,
                "news_id": 101,
                "title": "mock_comment_1",
                "date": "2023-12-01T11:00:00",
                "comment": "Mocked comment 1",
            },
            {
                "id": 202,
                "news_id": 101,
                "title": "mock_comment_2",
                "date": "2023-12-01T12:00:00",
                "comment": "Mocked comment 2",
            },
            {
                "id": 203,
                "news_id": 103,
                "title": "mock_comment_3",
                "date": "2023-12-03T16:00:00",
                "comment": "Mocked comment 3",
            },
        ],
        "comments_count": 3,
    }
    return news_data, comments_data


@pytest.fixture
async def client(aiohttp_client, mock_data):
    """
    Асинхронная фикстура для создания тестового клиента.
    Создает приложение aiohttp с моковыми данными и маршрутами.
    """
    app = web.Application()
    app["news_data"], app["comments_data"] = mock_data
    app.add_routes(routes)
    return await aiohttp_client(app)
