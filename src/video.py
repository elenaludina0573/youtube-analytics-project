import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""
    load_dotenv()
    api_key = os.getenv('YT_API_KEY')
    youtube = build('yuotube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """ Инициализация реальными данными следующих атрибутов экземпляра класса."""
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.video_id).execute()
        self.video_title: str = self.video_response["items"][0]["snippet"]["title"]
        self.video_url: str = f"https://youtu.be/{self.video_id}"
        self.view_count: int = self.video_response["items"][0]["statistics"]["viewCount"]
        self.like_count: int = self.video_response["items"][0]["statistics"]["likeCount"]


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id