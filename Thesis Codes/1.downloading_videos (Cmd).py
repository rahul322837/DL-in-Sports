from pytube import YouTube
import os

list_of_youtube_videos = []

file = open("data.csv", "r")
for line in file:
    line = line.split(",")
    link = 'https://www.youtube.com/watch?v=' + line[0]
    print(link)
    if link not in list_of_youtube_videos:
        list_of_youtube_videos.append(link)
print(list_of_youtube_videos)


#write code for inserting 1st column of csv file into list_of_youtube_videos
#assuming 1st column contains youtube links
#for example
def downloadvid_createdir(list_of_youtube_videos):
    for i in range(len(list_of_youtube_videos)):
        try:
            temp = list_of_youtube_videos[i]
            temp = temp[32:]
            #creating folder for each video
            path = "/Video_Files/failure/{0}".format(temp)
            #downloading each video
            video_link = list_of_youtube_videos[i]
            yt = YouTube(video_link).streams.filter(progressive=True, file_extension='mp4')
            yt.order_by('resolution')
            yt.desc()
            #yt.first()
            #print(yt.title)
            os.makedirs(path)
            yt.first().download(path,filename = 'vid')
            

        except OSError:  
            print ("Creation of the directory %s failed" % path)
        
        else:  
            print ("Successfully created the directory %s " % path)

downloadvid_createdir(list_of_youtube_videos)