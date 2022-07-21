#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     05.03.2021
# Copyright:   (c) SESA237770 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# pip install opencv-python
# pip install numpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()
##=============================================================================
import numpy as np
import cv2
import csv
##=============================================================================

def ExportMountingFrame(sPathFile,DataPoints):
    # field names
    fields = ['POSITION', 'X', 'Y']

    # data rows of csv file
##    DataPoints = [
##             ['TL', 'COE', '2', '9.0'],
##             ['BL', 'COE', '2', '9.1'],
##             ['BR', 'IT', '2', '9.3'],
##             ['TR', 'SE', '1', '9.5'],
##            ]

    with open(sPathFile, 'w',newline='') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(DataPoints )

def ImportMountingFrame(sPathFile):
     with open(sPathFile, mode ='r') as csvfile:

            csvReader = csv.reader(csvfile, delimiter=',')
            i=0
            MP_WORLD=[]
            for row in csvReader:
                print(row)

                MP_WORLD=  MP_WORLD + [(row[0],row[1],row[2])]
                i=i+1
     return MP_WORLD
##=============================================================================

# Create point matrix get coordinates of mouse click on image
X1=[0,1,0,0,0]
Y1=[0,1,0,0,0]
counter =1

X2=[0,0,0,0,0]
Y2=[0,0,0,0,0]

sCMD= 'command'
counter = 1
def mousePoints(event,x,y,flags,params):
    global counter
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        if (x < dim[0]) & (y < dim[1]) :
            print('Co-ordinate:',x,y)
            X1[counter] = x
            Y1[counter] = y
            counter = counter + 1
            if counter == 5 :
                counter = 1
    if event == cv2.EVENT_RBUTTONDOWN:
        if (x < dim[0]) & (y < dim[1]):
            print('Circle:',x,y)
            X2[1] = x
            Y2[1] = y
            print('Circle XY:',X2,Y2)




##=============================================================================
##cap = cv2.VideoCapture(0)
 # CAM
cap = cv2.VideoCapture(1)
 # FILE
##cap = cv2.VideoCapture('grey_img.png')

ret, frame = cap.read()

grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
scale_percent = 100 # percent of original size
width = int(grey_img.shape[1] * scale_percent / 100)
height = int(grey_img.shape[0] * scale_percent / 100)
dim = (width, height)



P1X= int(-width/3 + width/2)
P1Y= int(-height/3 + height/2)

P2X= int(+width/3 + width/2)
P2Y= int(-height/3 + height/2)

P3X= int(-width/3 + width/2)
P3Y= int(+height/3 + height/2)

P4X= int(+width/3 + width/2)
P4Y= int(+height/3 + height/2)

P5X= int( width/2)
P5Y= int( height/2)



X2=[0,int(width/2),0,0,0]
Y2=[0,int(height/2),0,0,0]

MountingFrame=[(P1X,P1Y),(P2X,P2Y),(P3X,P3Y),(P4X,P4Y),(P5X,P5Y)]

MP_WORLD= [('TL',P1X,P1Y),('BL',P2X,P2Y),('BR',P3X,P3Y),('TR',P4X,P4Y)] #mounting frame world


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
##=============================================================================
    # Our operations on the frame come here
##    frame = cv2.resize(frame, (400, 400))

##     grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    grey_img_2=grey_img
##=============================================================================
##    print('Original Dimensions : ',grey_img.shape)

    scale_percent = 100 # percent of original size
    width = int(grey_img.shape[1] * scale_percent / 100)
    height = int(grey_img.shape[0] * scale_percent / 100)
    dim = (width, height)







    # resize image
##    grey_img = cv2.resize(grey_img, dim, interpolation = cv2.INTER_AREA)
    grey_img_2 = grey_img.copy()


##    print('Resized Dimensions : ',resized.shape)

##=============================================================================

    # Display the resulting frame
    thresh = 128

##    grey_img_2 = cv2.cvtColor(grey_img_2, cv2.COLOR_BGR2GRAY)
##    if cv2.waitKey(1) & 0xFF == ord('b'):
##         grey_img_2 = cv2.threshold(grey_img_2, thresh, 255, cv2.THRESH_BINARY)[1]
##    cv2.line(img= grey_img_2, pt1=(10, 10), pt2=(100, 100), color=(0, 0, 0), thickness=5, lineType=8, shift=0)
##    cv2.circle(grey_img_2,(100,100), 20, (0,0,255),1)
##    cv2.rectangle(grey_img_2,(20,20),(180,180),(0,255,0),3)


    cv2.circle(grey_img_2,MountingFrame[0], 5, (0,0,255),2) #BGR
    cv2.circle(grey_img_2,MountingFrame[1], 5, (0,0,255),2)
    cv2.circle(grey_img_2,MountingFrame[2], 5, (0,0,255),2)
    cv2.circle(grey_img_2,MountingFrame[3], 5, (0,0,255),2)
    cv2.circle(grey_img_2,MountingFrame[4], 5, (0,0,255),2)

##    if counter == 1 :
##        cv2.circle(grey_img_2,MountingFrame[0], 5, (0,0,255),1)
##    if counter == 2 :
##        cv2.circle(grey_img_2,MountingFrame[1], 5, (0,0,255),1)
##    if counter == 3 :
##        cv2.circle(grey_img_2,MountingFrame[2], 5, (0,0,255),1)
##    if counter == 4 :
##        cv2.circle(grey_img_2,MountingFrame[3], 5, (0,0,255),1)
    # Draw Lines of Mounting Frame WORLD
    for POINT in MP_WORLD:
        try:
            cv2.circle(grey_img_2,(int(POINT[1]),int(POINT[2])), 10, (0,255,0),1)
##            print("",POINT)
        except:
##            print("Not integfer",POINT)
            dummmy=2


    # Draw Lines of Mounting Frame
    cv2.line(img= grey_img_2, pt1=(X1[4], Y1[4]), pt2=(X1[1], Y1[1]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[1], Y1[1]), pt2=(X1[2], Y1[2]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[2], Y1[2]), pt2=(X1[3], Y1[3]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[3], Y1[3]), pt2=(X1[4], Y1[4]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    # Make Export CSV
    DataPoints= [
                 ['TL',X1[1],Y1[1]],
                 ['BL',X1[2],Y1[2]],
                 ['BR',X1[3],Y1[3]],
                 ['TR',X1[4],Y1[4]]
                ]


##=============================================================================
# write PIXEL

    for i in [(100,100),(101,101),(101,100),(100,101)]:
        grey_img_2[ i[0] ][ i[1] ]  = 0

##    grey_img_2[ 15 ][ 15]  = [0, 0, 0]
##    grey_img_2[ X2[1] ][ Y2[1]]  = 255




# READ PIXEL
    for j in range(-10,10):
        sColorV = grey_img_2[ X2[1] ][ Y2[1]+j]
        sColorH = grey_img_2[ X2[1]+j ][ Y2[1]]

        sBrightnessV= (1*sColorV[0] + 1*sColorV[1] + 1*sColorV[2])/3
        sBrightnessH= (1*sColorH[0] + 1*sColorH[1] + 1*sColorH[2])/3
        sBrightness=int((sBrightnessV + sBrightnessH)/2/10) *10 # remove 1 digit


    if sBrightness > 50 :
        sONOFF='ON '
        nCircle=10
    else:
        sONOFF='OFF '
        nCircle=1

 # Draw circle for LED query
    cv2.circle(grey_img_2,(X2[1],Y2[1]), 5, (0,255,0),nCircle)

##    print('Circle LM:',X2[1],Y2[1])

##=============================================================================

##    rect = cv2.Rect(x, y, width, height)
##    region = image(rect)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (20, 10)
    # fontScale
    fontScale = 0.5
    # Blue color in BGR
    color = (0, 255, 0)
    # Line thickness of 2 px
    thickness = 1
    # Using cv2.putText() method
    sText="..."
    if counter==4:
            sText='Point TL '
    if counter==1:
            sText='Point BL '
    if counter==2:
            sText='Point BR '
    if counter==3:
            sText='Point TR '

    org = (20, 20)
    image = cv2.putText(grey_img_2, sONOFF + str(sBrightness), org, font,
                       fontScale, color, thickness, cv2.LINE_AA)
    org = (20, 40)
    image = cv2.putText(grey_img_2, sText + str(counter), org, font,
                       fontScale, color, thickness, cv2.LINE_AA)

    org = (200, 40)
    image = cv2.putText(grey_img_2, sCMD, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)

##=============================================================================
# KEYSTRIKE COMMANDS
    # EXPORT CSV
    if cv2.waitKey(1) & 0xFF == ord('e'):
        sPathFile='datapointsCAM.csv'
        ExportMountingFrame(sPathFile,DataPoints)
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV')
        print('')
        sCMD= 'EXPORTED POINTS'

    # IMPORT CSV
    if cv2.waitKey(1) & 0xFF == ord('i'):
        sPathFile='datapointsWORLD.csv'
        MP_WORLD=ImportMountingFrame(sPathFile)
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV')
        print(MP_WORLD)
        print('')
        sCMD= 'IMPORTED POINTS'


    # SAVE IMAGE
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('grey_img_1.png',grey_img)
        cv2.imwrite('grey_img_2.png',grey_img_2)

        print('EXPORT png')
        sCMD= 'EXPORTED IMAGES L & R'


    # QUIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
##=============================================================================
# IMAGE SHOW
    img_3 = np.concatenate((grey_img, grey_img_2), axis=1)

    cv2.imshow('frame',img_3)

    cv2.setMouseCallback('frame', mousePoints)
##=============================================================================
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()