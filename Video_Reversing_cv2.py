# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:54:24 2021

@author: Sanjay
"""

import cv2

# Video Capture Instance
cap = cv2.VideoCapture(r'D:\Misc\Extra\Sample.mp4')
                       

#Properties of Video

#Total number of frames in video  
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#Frames per second of video
fps = cap.get(cv2.CAP_PROP_FPS)

# height and width of video window
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#Initiating the Output writer for Video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('sample_reversed.avi', fourcc, fps, (int(width*0.75), int(height*0.75)))

print('No. of frames are {}'.format(frames))
print('FPS is {}'.format(fps))

# We get the index of the last frame of the video file
frame_index = frames-1

#Checking if the video instance is ready
if(cap.isOpened):
    
    #Reading till the end of the video
    while(frame_index!=0):
        
        # We set the current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        
        #Resize the frame
        frame = cv2.resize(frame, (int(width*0.75), int(height*0.75)))
        
        #OPTIONAL : To show the reversing video
		#cv2.imshow('winname', frame)
        
        #Writing the reversed video 
        out.write(frame)
        
        #Decrementing frame number in each step
        frame_index-=1
        
        #Show progress update
        if(frame_index%100==0):
            print(frame_index)
            
        #if(cv2.waitKey(5)==27):   ('27' in ASCII is Esc button)
           # break


out.release()
cap.release()

cv2.destroyAllWindows()
        
        
        
        
            
        