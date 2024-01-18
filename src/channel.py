import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = channel["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.subscriber_count = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.view_count = channel["items"][0]["statistics"]["viewCount"]
        self.data = {"title": self.title, "description": self.description, "url": self.url,
                     "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                     "view_count": self.view_count}

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        print(api_key)
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel))

    @classmethod
    def get_service(cls):
        """
         класс-метод ,
         возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, data):
        """
         метод, сохраняющий в файл значения
         атрибутов экземпляра `Channel`
        """
        with open("data_channel.json", "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            data = {"channel_id": self.channel_id, "title": self.title, "description": self.description,
                    "url": self.url, "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                    "view_count": self.view_count}

