#-------------------------------------------------------------------------------
# Name:        Transformations.py
# Purpose:
#
# Author:      SESA237770
#
# Created:     01.07.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##=============================================================================
import numpy as np
import csv
import os
##=============================================================================
def ExportMountingFrame(sPathFile,DataPoints):
    # field names
    ##    fields = ['POSITION', 'X', 'Y']
    # data rows of csv file
    ##    DataPoints = [
    ##
    ##             ['BL', 'COE', '2', '9.1'],
    ##             ['BR', 'IT', '2', '9.3'],
    ##             ['TR', 'SE', '1', '9.5'],
    ##             ['TL', 'COE', '2', '9.0'],
    ##            ]
    with open(sPathFile, 'w',newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
    ##        write.writerow(fields)
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
#========================================================
#========================================================
class transformation:
    ##  Class variables: This variable is shared between all objects of a class
    PTS_CAM=[['POSITION', 'X', 'Y']]
    PTS_GEOM =[['POSITION', 'X', 'Y']]
    PTS_WORLD_IN_CAM = [['POSITION', 'X', 'Y']]

    sPathFileCAM=''
    sPathFileWORLD=''
#========================================================
    def __init__(self, sPathFileCAM,sPathFileWORLD):

        ## class attributes
        self.XY_World=[['POSITION', 'X', 'Y']]
        self.sPathFileWORLD =[['POSITION', 'X', 'Y']]
        self.sPathFileCAM=sPathFileCAM
        self.sPathFileWORLD=sPathFileWORLD

#-------------------------------------------------------
    def transform_WORLD_IN_CAM_byscale(self,PTS_GEOM,PTS_CAM):

        print('=====transform_World_to_CAM_by_scale========================')
        print('')

        LXgeo=int(PTS_GEOM[0][1]) -int(PTS_GEOM[3][1])
        LXcam=int(PTS_CAM[0][1]) -int(PTS_CAM[3][1])
        LYgeo=int(PTS_GEOM[0][2]) -int(PTS_GEOM[2][2])
        LYcam=int(PTS_CAM[0][2]) -int(PTS_CAM[2][2])
        scaleX= abs(int(LXcam/LXgeo*100))
        scaleY= abs(int(LYcam/LYgeo*100))

        offsetX=PTS_CAM[0][1]
        offsetY=PTS_CAM[0][2]

        for item_in,item_out in zip(PTS_GEOM,PTS_CAM):

            for i in range(0,len(XY_World)):

                tempX=int(PTS_GEOM[i][1])*scaleX/100 +1*int(offsetX)
                tempY= int(PTS_GEOM[i][2])*scaleY/100 +1*int(offsetY)
                tempX=str(int(tempX))
                tempY= str(int(tempY))

                PTS_WORLD_IN_CAM[i]=(PTS_GEOM[i][0], tempX,tempY )

        print('===========================================================')


        return PTS_WORLD_IN_CAM
#----------------------------------------------------------
##=============================================================================
##=============================================================================
##=============================================================================
def main():
##        user = os.getlogin()
##        if user=='SESA237770':
##            sPrefix='MPA\\'
##        else: sPrefix='OJS\\'

        # Choose WORKSPACE"
        sJOBprefix='job_'
        sPrefix='workspace_MPA\\'
        sPrefix='workspace_OJS\\'
        sPrefix='workspace_2X2\\'
        sPrefix='workspace_1X2\\'

        sPrefix='workspace_1X2\\'
##=============================================================================
        print('')
        print('==============================================================')
        print('====Calculate the Transformation Equations====================')
        print('====COnvert job list from WORLD to CAMERA COORDINATES=========')
        print('==============================================================')
        print('')
#----------------------------------------------------------
    # IMPORT CSV
    # These points are used to create a transformation equations
        sPathFileImportCAMERA=sPrefix + 'MountingFrame_CAMERA.csv'
        sPathFileImportWORLD=sPrefix + 'MountingFrame_WORLD.csv'
        sPathFileImportTRANS_WORLD=sPrefix + 'MountingFrame_TRANS_WORLD.csv'

        sPathFileImportWORLD2=sPrefix + 'LED_WORLD.csv'
        sPathFileImportTRANS_WORLD2=sPrefix + 'LED_TRANS_WORLD.csv'

        WORLDS=[sPathFileImportWORLD,sPathFileImportWORLD2]
        TRANS_WORLDS=[sPathFileImportTRANS_WORLD,sPathFileImportTRANS_WORLD2]

        print('====IMPORT CSV=======PTS_CAM_MOUNTING_PLATE====================')
        print('IMPORT CSV MountingFrame Points from CAMERA   PTS_CAM')
        sPathFile=sPathFileImportCAMERA
        PTS_CAM=ImportMountingFrame(sPathFile)
##        print(PTS_CAM)

        print('====IMPORT CSV=========PTS_WORLD_MOUNTING_PLATE================')
        print('IMPORT WORLD MountingFrame Points from WORLD   PTS_GEOM')
        sPathFile=sPathFileImportWORLD
        PTS_GEOM=ImportMountingFrame(sPathFile)
##        print(PTS_PIXEL_GEOM)


        print('====IMPORT CSV=========PTS_WORLD_LED===========================')
        print('IMPORT WORLD LED Points from WORLD   PTS_LED')
        sPathFile=sPathFileImportWORLD
        PTS_LED=ImportMountingFrame(sPathFile)
##        print(PTS_PIXEL_GEOM)

#----------------------------------------------------------




        LXgeo=int(PTS_GEOM[0][1]) -int(PTS_GEOM[3][1])
        LXcam=int(PTS_CAM[0][1]) -int(PTS_CAM[3][1])
        LYgeo=int(PTS_GEOM[0][2]) -int(PTS_GEOM[2][2])
        LYcam=int(PTS_CAM[0][2]) -int(PTS_CAM[2][2])
        scaleX= abs(int(LXcam/LXgeo*100))
        scaleY= abs(int(LYcam/LYgeo*100))

        offsetX=PTS_CAM[0][1]
        offsetY=PTS_CAM[0][2]


        print('====Transformation Equations====')
        print('ScaleX:',scaleX)
        print('ScaleY:',scaleY)
        print('offsetX:',offsetX)
        print('offsetY:',offsetY)
        print('===============================\n')

        print('')
        print('==============================================================')
        print('====ITTERATION ALL POIT SETS FROM WORLD=======================')
        print('==============================================================')
        print('')
        for item_in,item_out in zip(WORLDS,TRANS_WORLDS):
            print('====IMPORT CSV======')
            print('IMPORT WORLD POINTS')
            sPathFile=sPathFileImportWORLD
            PTS_GEOM=ImportMountingFrame(item_in)
    ##        print(PTS_PIXEL_GEOM)
            print('')


            PTS_TRANS_WORLD=PTS_GEOM
            for i in range(0,len(PTS_GEOM)):

                tempX=int(PTS_GEOM[i][1])*scaleX/100 +1*int(offsetX)
                tempY= int(PTS_GEOM[i][2])*scaleY/100 +1*int(offsetY)
                tempX=str(int(tempX))
                tempY= str(int(tempY))

                PTS_TRANS_WORLD[i]=(PTS_GEOM[i][0], tempX,tempY )

##------------------------------------------------------------------------------
            print('===========================================================')
            print('====EXPORT CSV==========')
            print('EXPORT TRANS WORLD')
            sPathFile=item_out
            print('File:', sPathFile)
            ExportMountingFrame(sPathFile,PTS_TRANS_WORLD)
            [print(i) for i in PTS_TRANS_WORLD]
##            print(PTS_TRANS_WORLD)
            print('')
        print('===========================================================')

##=============================================================================

if __name__ == '__main__':

    main()

    print('')
    print('==============================================================')
    print('====TEST THE PROGRAM =======================')
    print('==============================================================')
    print('')

    sPrefix='MPA\\'
    sPathFileImport=sPrefix + 'MountingFrame_TRANS_WORLD.csv'
    sPathFileExport=sPrefix + 'MountingFrame_CAMERA.csv'

    sPathFileCAM=sPathFileImport
    sPathFileWORLD=sPathFileExport

    print( 'PATHS = ' , sPathFileCAM )
    print( 'PATHS = ' , sPathFileWORLD )

    TRANS=transformation(sPathFileCAM,sPathFileWORLD)
    print( 'Trans. = ' , TRANS.sPathFileCAM )
    print( 'Trans. = ' , TRANS.sPathFileWORLD )
##    transform_WORLD_IN_CAM_byscale(self,PTS_GEOM,PTS_CAM)


