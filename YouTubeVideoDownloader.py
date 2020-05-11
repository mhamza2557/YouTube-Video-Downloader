import os
import pytube
from pytube import YouTube
from pytube.cli import on_progress

print('''
  __  __   _    _     _    _                                   
 |  \/  | | |  | |   | |  | |                                  
 | \  / | | |__| |   | |__| |   __ _   _ __ ___    ____   __ _ 
 | |\/| | |  __  |   |  __  |  / _` | | '_ ` _ \  |_  /  / _` |
 | |  | | | |  | |   | |  | | | (_| | | | | | | |  / /  | (_| |
 |_|  |_| |_|  |_|   |_|  |_|  \__,_| |_| |_| |_| /___|  \__,_|
                                                               
                                                               
__     __      _______    _           __      ___     _            
\ \   / /     |__   __|  | |          \ \    / (_)   | |           
 \ \_/ /__  _   _| |_   _| |__   ___   \ \  / / _  __| | ___  ___  
  \   / _ \| | | | | | | | '_ \ / _ \   \ \/ / | |/ _` |/ _ \/ _ \ 
   | | (_) | |_| | | |_| | |_) |  __/    \  /  | | (_| |  __/ (_) |
   |_|\___/ \__,_|_|\__,_|_.__/ \___|     \/   |_|\__,_|\___|\___/ 
  
         _____                      _                 _           
        |  __ \                    | |               | |          
        | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
        | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
        | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
        |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|                                                                                                                                                                                                                                                             
''')


def filePath():
    home = os.path.expanduser('~')
    downloadPath =  os.path.join(home, 'Desktop')
    return downloadPath

url = input('Enter YouTube URL Here: ')
yt1 = YouTube(url, on_progress_callback=on_progress)
getResolution = yt1.streams.filter(progressive=True)

count = 0
for i in yt1.streams.filter(progressive=True):
    fileSize = (yt1.streams.filter(progressive=True, res=getResolution[int(count)].resolution).first().filesize) / (1024 * 1024)
    print(str(count) + ' ) ' + str(i.resolution) + ' - ' + str(i.mime_type) + ' - ' + str(float("{:.2f}".format(fileSize))) + ' MBs' )
    count = count + 1

inputResolution = input('\nEnter number # for resolution: ')
video = yt1.streams.filter(progressive=True, res=getResolution[int(inputResolution)].resolution).first()
video.download(filePath())

