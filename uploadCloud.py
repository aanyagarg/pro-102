import cv2
import dropbox
import time
import random

startTime = time.time()

def take_snapshot():
    generate = random.randint(0, 100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()

        imgName = "img" + str(generate) + ".png"  
        #img3.png

        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite(imgName,frame)
        result = False

    return imgName
    print("Your worst picture has been taken!!")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()



def uploading(imgName):
    accessToken = "7zj-_6rY66AAAAAAAAAAAXpdj7MfCe-MrwjbQTB4s30mjSZfC22hdaBlxscHQcJH"
    fileFrom = imgName
    fileTo = "/snapshots/" + imgName    
    dbx = dropbox.Dropbox(accessToken)

with open(fileFrom , 'rb') as f:
    dbx.files_uploads(f.read() , fileTo , mode=dropbox.files.WriteMode.overwrite)
    print("Uploaded!!!! ")



def main():
    while(True):
        if( (time.time() - startTime ) >= 5):
            name = take_snapshot()
            uploading(name)


main()







