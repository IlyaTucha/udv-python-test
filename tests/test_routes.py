import pytest


@pytest.mark.asyncio
async def test_get_active_news_list(client):
    """Тест на проверку получения списка неудаленных новостей и их количества"""
    resp = await client.get("/")
    assert resp.status == 200
    data = await resp.json()

    assert "news" in data
    assert "news_count" in data
    assert data["news_count"] == 2

    first_news = data["news"][0]
    assert first_news["id"] == 101
    assert first_news["comments_count"] == 2


@pytest.mark.asyncio
async def test_get_existing_news_by_id(client):
    """Тест на проверку получения существующей новости по её идентификатору"""
    resp = await client.get("/news/101")
    assert resp.status == 200
    data = await resp.json()

    assert "id" in data
    assert "title" in data
    assert "comments" in data
    assert data["id"] == 101
    assert len(data["comments"]) == 2


@pytest.mark.asyncio
async def test_get_deleted_news_by_id(client):
    """Тест на проверку получения удаленной новости"""
    resp = await client.get("/news/102")
    assert resp.status == 404
    text = await resp.text()
    assert text == "404: News not found"


@pytest.mark.asyncio
async def test_get_nonexistent_news_by_id(client):
    """Тест на проверку получения несуществующей новости"""
    resp = await client.get("/news/999")
    assert resp.status == 404
    text = await resp.text()
    assert text == "404: News not found"


@pytest.mark.asyncio
async def test_get_news_by_negative_id(client):
    """Тест на проверку получения новости с отрицательным ID"""
    resp = await client.get("/news/-1")
    assert resp.status == 404
    text = await resp.text()
    assert text == "404: News not found"


@pytest.mark.asyncio
async def test_get_news_by_invalid_id_format(client):
    """Тест на проверку получения новости с неверным форматом ID (буквы вместо числа)"""
    resp = await client.get("/news/abc")
    assert resp.status == 404
    text = await resp.text()
    assert text == "404: News not found"
