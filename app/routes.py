from aiohttp import web
from .models import NewsData, CommentsData
from .utils import group_comments_by_news_id

routes = web.RouteTableDef()


@routes.get("/")
async def get_news_list(request) -> web.Response:
    try:
        news_data = NewsData.model_validate(request.app["news_data"])
        comments_data = CommentsData.model_validate(request.app["comments_data"])

        comments_by_news_id = group_comments_by_news_id(comments_data)

        active_news = []
        for news_item in news_data.news:
            if news_item.deleted:
                continue

            news_comments = comments_by_news_id.get(news_item.id, [])

            news_item_dict = news_item.model_dump(mode="json")
            news_item_dict["comments_count"] = len(news_comments)
            active_news.append(news_item_dict)

        return web.json_response({"news": active_news, "news_count": len(active_news)})
    except Exception as e:
        return web.Response(status=500, text=f"500: Error processing data: {str(e)}")


@routes.get("/news/{news_id}")
async def get_news_by_id(request) -> web.Response:
    try:
        news_data = NewsData.model_validate(request.app["news_data"])
        comments_data = CommentsData.model_validate(request.app["comments_data"])

        news_item = None
        try:
            news_id = int(request.match_info["news_id"])
            for item in news_data.news:
                if item.id == news_id and not item.deleted:
                    news_item = item
                    break
        except ValueError:
            pass

        if not news_item:
            return web.Response(status=404, text="404: News not found")

        comments_by_news_id = group_comments_by_news_id(comments_data)
        news_comments = comments_by_news_id.get(news_id, [])

        news_details = news_item.model_dump(mode="json")
        news_details["comments"] = [
            comment.model_dump(mode="json") for comment in news_comments
        ]
        news_details["comments_count"] = len(news_comments)

        return web.json_response(news_details)
    except Exception as e:
        return web.Response(status=500, text=f"500: Error processing data: {str(e)}")
