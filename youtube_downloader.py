from __future__ import unicode_literals
import youtube_dl
import os


class YoutubeDownloader:

    def __init__(self, key = 'FFmpegExtractAudio', codec = 'mp3', quality = '192'):


        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': key,
                'preferredcodec': codec,
                'preferredquality': quality,
            }],
            'progress_hooks': [self.progress_channged],
            'outtmpl': 'static/%(title)s-%(id)s.mp3'
        }

        self.downlaoder =  youtube_dl.YoutubeDL(ydl_opts)
    
    def progress_channged(self, data):
        
        if data['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(data['filename']))
            self.url = '/' + data['filename']
            print("Done downloading {}".format(file_tuple[1]))
        if data['status'] == 'downloading':
            p = data['_percent_str']
            p = p.replace('%','')
            #self.progress.setValue(float(p))
            print(data['filename'], data['_percent_str'], data['_eta_str'])

    def downlaod(self, urls):
        ret_code = self.downlaoder.download(urls)

if __name__ == '__main__':
    donwloader = YoutubeDownloader()
    donwloader.downlaod(['https://www.youtube.com/watch?v=5aqQ0wq0c_4'])