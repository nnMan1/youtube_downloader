from __future__ import unicode_literals
import youtube_dl


class YoutubeDownloader:

    def __init__(self, key = 'FFmpegExtractAudio', codec = 'mp3', quality = '192'):


        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': key,
                'preferredcodec': codec,
                'preferredquality': quality,
            }],
        }

        self.downlaoder =  youtube_dl.YoutubeDL(ydl_opts)
    
    def downlaod(self, url)
        self.downlaoder.download(url)