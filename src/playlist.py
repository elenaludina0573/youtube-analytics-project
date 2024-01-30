import os
from dotenv import load_dotenv
import isodate
from datetime import timedelta
from googleapiclient.discovery import build


class PlayList:
    """Класс для ютуб-канала"""
    load_dotenv()
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
        self.response = self.youtube.playlists().list(id=self._playlist_id,
                                                      part='snippet',
                                                      ).execute()
        self.title = self.response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self._playlist_id}"

    def __str__(self):
        return f"{self.title}"

    @property
    def total_duration(self) -> timedelta:
        self._playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
        playlist_videos = self.youtube.playlistItems().list(playlistId=self._playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        total_duration: timedelta = timedelta(hours=0, minutes=0, seconds=0)
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
            return total_duration

    def show_best_video(self):
        max_like_count = 0
        max_video_id = 0
        for video in self.video_response['items']:
            like_count: int = video['statistics']['likeCount']
            video_id = video['id']
            if int(like_count) > int(max_like_count):
                max_like_count = like_count
                max_video_id = video_id
                return f"https://youtu.be/{max_video_id}"
