import pytube
from pytube import YouTube
from pytube.cli import on_progress

url = input('Enter YouTube URL Here: ')
yt1 = YouTube(url, on_progress_callback=on_progress)
getResolution = yt1.streams.filter(adaptive=True, mime_type="video/mp4")

count = 0
for i in yt1.streams.filter(adaptive=True, mime_type="video/mp4"):
    fileSize = (yt1.streams.filter(adaptive=True, mime_type="video/mp4", res=getResolution[count].resolution).first().filesize) / (1024 * 1024)
    print(str(count) + ' ) ' + str(i.resolution) + ' - ' + str(i.mime_type) + ' - Approx: ' + str(float("{:.2f}".format(fileSize))) + ' MBs' )
    count = count + 1

inputResolution = input('\nEnter number # for resolution: ')
print(yt1.streams.filter(adaptive=True, mime_type="video/mp4", res=getResolution[int(inputResolution)].resolution).first())
video = yt1.streams.filter(adaptive=True, mime_type="video/mp4", res=getResolution[int(inputResolution)].resolution).first()
video.download()