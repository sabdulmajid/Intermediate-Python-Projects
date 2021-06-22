# DownloadingYouTubeVideosMP3.py
from tube_dl import Youtube

Youtube('https://www.youtube.com/watch?v=wvZAX1Gymhg').formats.filter(only_audio=True)[0].download(convert='mp3')
