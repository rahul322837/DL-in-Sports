
# coding: utf-8

# In[1]:


from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# In[2]:


import os
import sys
import subprocess as sp
import cv2

from moviepy.tools import subprocess_call
from moviepy.config import get_setting


# In[3]:


def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ Makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    name, ext = os.path.splitext(filename)
    if not targetname:
        #T1, T2 = [int(t*1000) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, t1, t2, ext)
    
    cmd = [get_setting("FFMPEG_BINARY"),"-y",
           "-ss", "%0.2f"%(t1/1000),
           "-i", filename,
           "-t", "%0.2f"%((t2-t1)/1000),
           "-vcodec", "copy", "-acodec", "copy", targetname]
    
    subprocess_call(cmd)


# In[8]:


file = open('3 videos.csv', "r")

time_stamp = []
#for line in file:
    #print(line)
    #line = line.split(",")
    #line = [line[0], line[9], float(line[5]), float(line[6])]
    #time_stamp.append(line)
#print(time_stamp)

for line in file:
    line = line.split(',')
    line = [line[0], line[9], float(line[5]), float(line[6])]
    if (line not in time_stamp) and (line[3]-line[2] <= 5000):
        time_stamp.append(line)

for i in time_stamp:
    if "failure" in i[1]:
        i[1] = "failure"
    elif "success" in i[1]:
        i[1] = "success"
#print(time_stamp, "\n")
#print(len(time_stamp))

for i in time_stamp:
    if i[2] < 0:
        continue
    else:
        if i[1] == "failure":
            location = 'A:\\Users\\aakashwadhwa\\Desktop\\failure\\' + i[0] + '\\vid.mp4'
            ffmpeg_extract_subclip(location, i[2], i[3], None, )
        else:
            location = 'A:\\Users\\aakashwadhwa\\Desktop\\success\\' + i[0] + '\\vid.mp4'
            ffmpeg_extract_subclip(location, i[2], i[3], None)

        





