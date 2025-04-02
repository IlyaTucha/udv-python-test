from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def get_news_list(request) -> web.Response:
    news_data = request.app["news_data"]
    comments_data = request.app["comments_data"]

    active_news = []

    for news_item in news_data["news"]:
        if news_item["deleted"]:
            continue

        comments_count = 0
        for comment in comments_data["comments"]:
            if comment["news_id"] == news_item["id"]:
                comments_count += 1

        news_with_comments_count = dict(news_item)
        news_with_comments_count["comments_count"] = comments_count
        active_news.append(news_with_comments_count)

    return web.json_response({"news": active_news, "news_count": len(active_news)})


@routes.get("/news/{news_id}")
async def get_news_by_id(request) -> web.Response:
    news_data = request.app["news_data"]
    comments_data = request.app["comments_data"]

    news_id = int(request.match_info["news_id"])

    news_item = None
    for item in news_data["news"]:
        if item["id"] == news_id:
            news_item = item
            break

    if not news_item or news_item["deleted"]:
        return web.Response(status=404, text="News not found")

    news_comments = []
    for comment in comments_data["comments"]:
        if comment["news_id"] == news_id:
            news_comments.append(comment)

    news_details = dict(news_item)
    news_details["comments"] = news_comments
    news_details["comments_count"] = len(news_comments)

    return web.json_response(news_details)
