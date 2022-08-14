from youtubesearchpython import VideosSearch
from pytube import YouTube
import os
import pandas

count=1
def search(song,c):
    videosSearch = VideosSearch(song, limit = 1)
    s=videosSearch.result()
    d=s['result'][0]['link']
    down(d,c)

def down(d,c):
    # url input from user
    yt = YouTube(str(d))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    destination = "music/"
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(c,yt.title + " has been successfully downloaded.")


  
# csv file name
filename = "shazamlibrary.csv"
  

df = pandas.read_csv(filename,header=1)
# df = pandas.read_csv(filename)
# df = df.iloc[1:, :]
dd=df['Title']
da=df['Artist']
j=0
sngs=[]
nsngs=[]
for i in dd:
    # search(i)

    b=(i+" "+da[j])
    # print(b.decode('utf-8'))
    if b not in sngs:
        sngs.append(b)
    else:
        nsngs.append(b)
    j=j+1
c=1
for i in sngs:
    try:
        search(i,c)
    except:
        pass
    c=c+1
