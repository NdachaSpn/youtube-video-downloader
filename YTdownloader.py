pip install pytube
#this installs neccesary liblary
from pytube import YouTube
link= input("enter your url : ")
yt=YouTube(link)
videos=yt.streams.all()

video=list(enumerate(videos))

for i in video:
	print (i)
	#this will print all video formats availlable
print("enter the desired output format : ")
dn_option=int(input("enter the option : "))

dn_videos=videos[dn_option]
dn_videos.download()

print("download complete")