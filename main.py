from aiohttp import web
from app.routes import routes
from app.data_loader import init_data

app = web.Application()

news_data, comments_data = init_data()
app["news_data"] = news_data
app["comments_data"] = comments_data

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8080)
