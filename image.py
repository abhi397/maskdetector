

'''
    cap = cv2.VideoCapture(0);
fcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fcc, 20.0, (640,480))
while True:
    ret , frame = cap.read()
    output.write(frame)
    cv2.imshow('frame' , frame)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
output.release()
cv2.destroyAllWindows()
'''
import cv2
import logging
import os
import random
import string

def rand_string(length):
    """generates a rando string of numbers,lower and uppercase chars"""
    rand_str=''.join(random.choice(
                string.ascii_lowercase
                +string.ascii_uppercase
                +string.digits)
            for i in range(length))
    return rand_str


def length_of_video(video_path):
    """helper function"""
    cap=cv2.VideoCapture(video_path)
    length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length



def extracting_frames(video_path,save_path,skip_frames=10):
    """extract frames from video and save as jpg"""

    print('*****ENTERING EXTRACTING PHRASE*****')

    #C:\Users\Asus\PycharmProjects\imagedetector\output.avi
    _,file_name=os.path.split(video_path)

    #output.avi
    file_name_without_ext=os.path.splitext(file_name)[0]


    #check length
    length=length_of_video(video_path)
    if length==0:
        print('length is 0,exiting extracting phrase')
        return 0

    cap=cv2.VideoCapture(video_path)
    count=0
    random_string=rand_string(5)

    ret,frame=cap.read()#ret frame returned correctly
    test_file_path=os.path.join(
                save_path,
                file_name_without_ext[:6]+\
                '{}_{}.jpg'.format(random_string,count)
    )


    cv2.imwrite(test_file_path,frame)
    if os.path.isfile(test_file_path):
        print('saving test frame was sucessfull, '+
              'Continuing Extraction phrase')

        count=1
        while ret:
            ret,frame=cap.read()
            if ret and count%skip_frames==0:
                cv2.imwrite(os.path.join(
                         save_path,
                         file_name_without_ext[:6]+
                         '{}_{}.jpg'.format(random_string,count)),frame
                )
                count+=1
                print(count)
            else:
                count+=1

        else:
            print('Problem with saving Test frame cv2 encoding cannot save file ')
            return 0

        cap.release()
        print('******Finished Extraction*******')

        if __name__=="__main__":
            public_movies=["output.avi"]
            save_path="images"
            for movie in public_movies:
                print(movie)
                extracting_frames(movie,save_path,skip_frames=10)









