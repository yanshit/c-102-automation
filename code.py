import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject= cv2.VideoCaptureObject(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False

    return image_name
    print("Snapshot Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindow()

take_snapshot()

def upload_file(image_name):
    access_token='sl.A2_IaEvjThE5i6vvUx-nrfaWwrZRhc_GeijTC5GO5aDhWtpmKYtrXNwjkuNiqZRC62O23xB13ntD_kfBAIKhJjSXoK-wxrt75rEZCHt1gqYEc2HJhSODPLJFHwYFKXpl3ZfVYYU'
    file = image_name
    file_from=file
    file_to="/newFolder1"+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=3):
            name=take_snapshot()
            upload_file=(name)


main()     





