import sys
import os
import dlib
import glob
import cv2  #opencv 사용
import math
import numpy as np
import openface
import shutil
#opencv에서 ESC 키입력 상수
ESC_KEY = 27

'''
RGB > BGR or BGR > RGB 변환 
dlib는 RGB 형태로 이미지를 사용하고
openCV는 BGR 형태이므로 B와 R을 바꿔주는 함수가 필요하다.
'''
def createFolder(dir):
    try:
        # 폴더가 없으면 생성
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
    
        # if os.path.exists(dir+str("/face_eyebrow")):
        #     shutil.rmtree(dir+str("/face_eyebrow"))
        # os.makedirs(dir+str("/face_eyebrow"))

        # if os.path.exists(dir+str("/face_eye")):
        #     shutil.rmtree(dir+str("/face_eye"))
        # os.makedirs(dir+str("/face_eye"))

        # if os.path.exists(dir+str("/face_nose")):
        #     shutil.rmtree(dir+str("/face_nose"))
        # os.makedirs(dir+str("/face_nose"))

        # if os.path.exists(dir+str("/face_mouse")):
        #     shutil.rmtree(dir+str("/face_mouse"))
        # os.makedirs(dir+str("/face_mouse"))
        
    except OSError:
        print("Error: Creating directory."+ dir)
        
def swapRGB2BGR(rgb):
    r, g, b = cv2.split(img)
    bgr = cv2.merge([b,g,r])
    return bgr

def extractMouse(faceImg,l,num):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(48,68):
        x = l.part(i).x
        y = l.part(i).y
        if x < faceImg.shape[1]:
            locX.append(x)
        if y < faceImg.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)-3
    bottom = max(locY)+5
    left = min(locX)
    left = left-10 if left-10 > 0 else 0
    right = max(locX)
    right = right+10 if right+10 < faceImg.shape[1] else faceImg.shape[0]-1
   
    # 입를 추출한다.
    tempImg = faceImg[top:bottom,left:right]
    
    # M = np.float32([[1,0,0],[0,1,0]])
    # mouseImg = cv2.warpAffine(tempImg,M,(100,100),borderValue=(255,255,255))

    # cv2.imwrite(outDir+"/face_mouse/{}.jpg".format(num),tempImg)
    cv2.imwrite(outDir+"/{}.jpg".format(num),tempImg)

    return 

def extractNose(faceImg,l,num):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(28,36):
        x = l.part(i).x
        y = l.part(i).y
        if x < faceImg.shape[1]:
            locX.append(x)
        if y < faceImg.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)
    bottom = max(locY)+5
    left = min(locX)
    left = left-15 if left-15 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < faceImg.shape[1] else faceImg.shape[0]-1
   
    # 코를 추출한다.
    tempImg = faceImg[top:bottom,left:right]
    
    # M = np.float32([[1,0,0],[0,1,0]])
    # noseImg = cv2.warpAffine(tempImg,M,(100,100),borderValue=(255,255,255))
    # cv2.imwrite("./images/output/face_nose/{}.jpg".format(num),tempImg)

    #cv2.imwrite(outDir+"/face_nose/{}.jpg".format(num),tempImg)
    cv2.imwrite(outDir+"/{}.jpg".format(num),tempImg)


def extractEyebrows(faceImg,l,num):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(17,26):
        x = l.part(i).x
        y = l.part(i).y
        if x < faceImg.shape[1]:
            locX.append(x)
        if y < faceImg.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)
  
    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)
    top = top-5 if top-5 > 0 else 0
    bottom = max(locY)+5
    left = min(locX)
    left = left-5 if left-5 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < faceImg.shape[1] else faceImg.shape[0]-1

    # 눈썹을 추출한다.
    tempImg = faceImg[top:bottom,left:right]
     
    # 0.0 위치로 이동시킨후에 고정 사이즈로 통합한다.
    # M = np.float32([[1,0,0],[0,1,0]])
    # eyebrowImg = cv2.warpAffine(tempImg,M,(200,50),borderValue=(255,255,255))    
    
    # 번호를 매겨 저장한다.
    #cv2.imwrite("./images/output/face_eyebrow/{}.jpg".format(num),tempImg)

    cv2.imwrite(outDir+"/face_eyebrow/{}.jpg".format(num),tempImg)

def extractEyes(faceImg, l, num):    
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(36,48):
        x = l.part(i).x
        y = l.part(i).y
        if x < faceImg.shape[1]:
            locX.append(x)
        if y < faceImg.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 가장 가장자리인 영역들을 추출한다.
    top = min(locY)
    top = top-5 if top-5 > 0 else 0
    bottom = max(locY)+5
    left = min(locX)
    left = left-15 if left-15 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < faceImg.shape[1] else faceImg.shape[0]-1

    tempImg = faceImg[top:bottom,left:right]

    # 0.0 위치로 이동시킨후에 고정 사이즈로 통합한다.
    # M = np.float32([[1,0,0],[0,1,0]])
    # eyeImg = cv2.warpAffine(tempImg,M,(200,50),borderValue=(255,255,255))    
    
    # 번호를 매겨 저장한다.    
    #cv2.imwrite(outDir+"/face_eye/{}.jpg".format(num),tempImg)
    cv2.imwrite(outDir+"/{}.jpg".format(num),tempImg)


'''
매개변수가 3개여야 한다.
'''
if len(sys.argv) != 3:
    print(
        "Give the path to the trained shape predictor model as the first "
        "argument and then the directory containing the facial images.\n"
        "For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
        "You can download a trained facial shape predictor from:\n"
        "    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
    exit()

# 랜드마크 파일 경로
predictor_path = sys.argv[1]

# 이미지 경로
faces_folder_path = sys.argv[2]

# 얼굴 인식용 클래스 생성 (기본 제공되는 얼굴 인식 모델 사용)
face_detector = dlib.get_frontal_face_detector()

# 인식된 얼굴에서 랜드마크 찾기위한 클래스 생성 
face_pose_detector = dlib.shape_predictor(predictor_path)

# 얼굴을 정렬할 클래스 생성 - Openface
face_aligner = openface.AlignDlib(predictor_path)

# 순서 매길 값 
cnt = 1

# print(faces_folder_path)
name = faces_folder_path[10:-1]
# print(name)

outDir = "./res/output/"+name
createFolder(outDir)

# 두번째 매개변수로 지정한 폴더의 모든 jpg 파일들을 읽는다.
for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):

    # 파일명을 출력한다.
    #print("Processing file: {}".format(f))
    
    # 파일에서 이미지 불러오기
    img = dlib.load_rgb_image(f)      
    
    # 불러온 이미지 데이터의 채널 R과 B를 바꿔준다. dlib와 cv2는 채널모양이 다름. 
    cvImg = swapRGB2BGR(img)    

    # 얼굴 인식, 1은 샘플링 값
    dets = face_detector(img, 1)

    # 인식한 얼굴에서 랜드마크를 생성.(얼굴이 1개인 단일이미지로 가정한다)
    landmarks = face_pose_detector(img, dets[0])

    # 19 = 왼쪽 눈썹 중앙, 24 = 오른쪽 눈썹 중앙, 8 = 턱선 중앙 
    # 세 좌표가 같은 위치에 오도록 하여 정렬한다
    faceImg = face_aligner.align(200,cvImg,dets[0],landmarkIndices=[19,24,33])
    #faceImg = face_aligner.align(200,cvImg,dets[0],landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    # 정렬된 영상으로 다시 얼굴을 인식하여 랜드마크를 생성한다.
    d = face_detector(faceImg,1)
    if len(d) == 0:
        continue
    l = face_pose_detector(faceImg,d[0])

    # 순서대로 눈썹, 눈 추출
    #extractEyebrows(faceImg,l,cnt)
    #extractEyes(faceImg,l,cnt)
    #extractNose(faceImg,l,cnt)
    extractMouse(faceImg,l,cnt)
    cnt+=1
    #cv2.imshow('Origin',cvImg)
    #cv2.imshow('AlignedFace',faceImg)
    # 무한 대기를 타고 있다가 ESC 키가 눌리면 빠져나와 다음 이미지를 검색한다.
    #while True:
    #    if cv2.waitKey(0) == ESC_KEY:
    #        break;

#cv2.destroyWindow('Face')   

