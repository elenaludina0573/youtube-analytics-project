import os
from dotenv import load_dotenv
from src.channel import Channel
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""
    load_dotenv()
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """ Инициализация реальными данными следующих атрибутов экземпляра класса."""
        self.video_id = video_id
        youtube = Channel.get_service()

        video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                      id=video_id
                                      ).execute()
        try:
            self.video_url: str = f"https://youtu.be/{self.video_id}"
            self.title = video['items'][0]['snippet']['title']
            self.view_count = video['items'][0]['statistics']['viewCount']
            self.like_count = video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return f"{self.video_title}"

    
class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{self.video_title}"

