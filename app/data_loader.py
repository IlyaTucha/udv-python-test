import json


def init_data():
    with open("data/news.json", "r") as f:
        news = json.load(f)
    with open("data/comments.json", "r") as f:
        comments = json.load(f)
    return news, comments
