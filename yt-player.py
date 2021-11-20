import time as t
import vlc
import pafy

url = input('Enter the YouTube video URL here:')
print('Creating pafy object...')
video = pafy.new(url)
print('Getting the higest quality version of the video...')
best = video.getbest()
print('Creating VLC media player object...')
media = vlc.MediaPlayer(best.url)
media.play()
print('Playing video...')
input()
