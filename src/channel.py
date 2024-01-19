import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
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
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
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

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id

    def to_json(self, data):
        """
         метод, сохраняющий в файл значения
         атрибутов экземпляра `Channel`
        """
        with open("moscowpython.json'", "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            data = {"channel_id": self.__channel_id, "title": self.title, "description": self.description,
                    "url": self.url, "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                    "view_count": self.view_count}
            print(data)

    def __str__(self):
        return f'{self.title}, {self.url}'

    def __add__(self, other):
        result_1 = self.subscriber_count + other.subscriber_count
        return result_1

    def __sub__(self, other):
        result_2 = int(self.subscriber_count) - int(other.subscriber_count)
        return result_2

    def __rsub__(self, other):
        result_3 = self.subscriber_count - other.subscriber_count
        return result_3

    def __gt__(self, other):
        result_4 = self.subscriber_count > other.subscriber_count
        return result_4

    def __ge__(self, other):
        result_5 = self.subscriber_count >= other.subscriber_count
        return result_5

    def __lt__(self, other):
        result_6 = self.subscriber_count < other.subscriber_count
        return result_6

    def __le__(self, other):
        result_7 = self.subscriber_count <= other.subscriber_count
        return result_7

    def __eq__(self, other):
        result_8 = self.subscriber_count == other.subscriber_count
        return result_8
