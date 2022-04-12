# Simple youtube downloader that asks users for input (url and wheter users
# want audio or video files) and saves specified files in the current directory.

# pip install pytube
from pytube import YouTube
from sys import exit

url = str(input('Enter full YouTube URL: '))

try:
  yt = YouTube(url)
  title = yt.title
except:
  print('Something went wrong. Please try again')
  exit()

action = str(input('Do you want to download video or audio only? (audio/video): ')).lower()

if action == 'audio':
  audio = yt.streams.get_audio_only().download()

elif action == 'video':
  video = yt.streams.get_highest_resolution().download()

else:
  print('Wrong value!')
  exit()
  
