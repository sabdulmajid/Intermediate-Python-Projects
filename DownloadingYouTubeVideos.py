# DownloadingYouTubeVideos.py
# Very simple way to download YouTube videos using Python Web-Scraping.

from __future__ import unicode_literals
import youtube_dl


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/playlist?list=PLLQoKlevNVshQMKiCsmT3Sgw4gOAo4mM8"])
