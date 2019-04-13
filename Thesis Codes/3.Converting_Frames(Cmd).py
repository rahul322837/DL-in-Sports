import cv2
import os

#videocap = cv2.VideoCapture('A:/Study/Python/data/{}/vid1.mp4'.format(i[0]))

#success,image = vidcap.read()

#import matplot.pyplot as pyplot
#plt.imshow(image)

def createfolder(direc):
    try:
        if not os.path.exists(direc):
            os.makedirs(direc)
    except OSError:
        print("Error creating directory"+direc)
            
file = open('3 videos.csv','r')

time_stamp = []
video_list = []
for line in file:
    line = line.split(',')
    line = [line[9],float(line[5]),float(line[6]),line[0]]
    if (line not in time_stamp) and (line[2]-line[1] <= 5000):
        time_stamp.append(line)

for line in time_stamp:
    #line = line.split(',')
    line = line[3]
    if line not in video_list:
        video_list.append(line)
#print(time_stamp)
print(video_list)
    

filelist = os.listdir( 'A:/Users/aakashwadhwa/Desktop' )
print(filelist)

for fs in filelist:
    for id in video_list:
        filelist2 = os.listdir( 'A:/Users/aakashwadhwa/Desktop/{}/{}'.format(fs,id) )
        print(filelist2)
        for sv in filelist2:
            if sv == "vid.mp4":
                continue   
            vidcap = cv2.VideoCapture('A:/Users/aakashwadhwa/Desktop/{}/{}/{}'.format(fs, id,sv))
            success,image = vidcap.read()
            count = 0
            frame_ctr = 0
            success = True
            if fs == 'failure':
                while success:
                    if count%1 == 0:
                        path_p1 = 'A:/Study/Python/data/failure/{}'.format(sv)
                        createfolder(path_p1)
                        cv2.imwrite(path_p1+'/frame%d.jpg'%frame_ctr,image)
                        frame_ctr+=1
                        success, image = vidcap.read()
                        count+=1
            else:
                while success:
                    if count%1 == 0:
                        path_p1 = 'A:/Study/Python/data/success/{}'.format(sv)
                        createfolder(path_p1)
                        cv2.imwrite(path_p1+'/frame%d.jpg'%frame_ctr,image)
                        frame_ctr+=1
                        success, image = vidcap.read()
                        count+=1
                    
