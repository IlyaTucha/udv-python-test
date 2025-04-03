from typing import List
from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: datetime
    comment: str


class CommentsData(BaseModel):
    comments: List[Comment]
    comments_count: int


class NewsItem(BaseModel):
    id: int
    title: str
    date: datetime
    body: str
    deleted: bool


class NewsData(BaseModel):
    news: List[NewsItem]
    news_count: int
