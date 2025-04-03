from typing import Dict, List
from .models import CommentsData


def group_comments_by_news_id(comments_data: CommentsData) -> Dict[int, List]:
    """Группирует комментарии по идентификатору новости для оптимизации поиска."""
    comments_by_news_id = {}
    for comment in comments_data.comments:
        news_id = comment.news_id
        if news_id not in comments_by_news_id:
            comments_by_news_id[news_id] = []
        comments_by_news_id[news_id].append(comment)
    return comments_by_news_id
