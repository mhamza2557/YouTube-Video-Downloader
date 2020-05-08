import os
import pytube
from pytube import YouTube
from pytube.cli import on_progress

def filePath():
    home = os.path.expanduser('~')
    downloadPath =  os.path.join(home, 'Desktop')
    return downloadPath

url = input('Enter YouTube URL Here: ')
yt1 = YouTube(url, on_progress_callback=on_progress)
getResolution = yt1.streams.filter(adaptive=True)

count = 0
for i in yt1.streams.filter(adaptive=True):
    fileSize = (yt1.streams.filter(adaptive=True, res=getResolution[int(count)].resolution).first().filesize) / (1024 * 1024)
    print(str(count) + ' ) ' + str(i.resolution) + ' - ' + str(i.mime_type) + ' - ' + str(float("{:.2f}".format(fileSize))) + ' MBs' )
    count = count + 1

inputResolution = input('\nEnter number # for resolution: ')
print(yt1.streams.filter(adaptive=True, res=getResolution[int(inputResolution)].resolution).first())
video = yt1.streams.filter(adaptive=True, res=getResolution[int(inputResolution)].resolution).first()
video.download(filePath())

