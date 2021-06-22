# DownloadingVideosWithPytube - TEST.py
from pytube import YouTube

link = input('Enter the link of the video:  ')
yt = YouTube(link)

print('Title: ', yt.title)
print('Number of views: ', yt.views)
print('Length of video: ', yt.length, 'seconds')
print('Description: ', yt.description)
print('Ratings: ', yt.rating)

print(yt.streams)

print(yt.streams.filter(only_video=True))

ys = yt.streams.get_highest_resolution()

print(ys)

print('Downloading...')
ys.download('c:\\Users\\shaik\\Desktop\\Videos')
print('Download completed!')
