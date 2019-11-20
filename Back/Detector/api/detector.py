import sys
import os
import dlib
import glob
import cv2  #opencv 사용
import math
import numpy as np
import openface
import shutil
from django.conf import settings
from .models import Image


# opencv에서 ESC 키입력 상수
ESC_KEY = 27
CIRCLE_SIZE = 6
# 랜드마크 파일 경로
predictor_path = settings.BASE_DIR+"/api/res/shape_predictor_68_face_landmarks.dat"

'''
RGB > BGR or BGR > RGB 변환 
dlib는 RGB 형태로 이미지를 사용하고
openCV는 BGR 형태이므로 B와 R을 바꿔주는 함수가 필요하다.
'''
        
def swapRGB2BGR(img):
    r, g, b = cv2.split(img)
    bgr = cv2.merge([b,g,r])
    return bgr

# l = landmark
def extractMouse(img,l,name):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 입의 좌표들을 종합한다(48 ~ 67)
    for i in range(48,68):
        x = l.part(i).x
        y = l.part(i).y
        if x < img.shape[1]:
            locX.append(x)
        if y < img.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)-3
    bottom = max(locY)+5
    left = min(locX)
    left = left-10 if left-10 > 0 else 0
    right = max(locX)
    right = right+10 if right+10 < img.shape[1] else img.shape[0]-1
   
    # 입을 추출한다.
    tempImg = img[top:bottom,left:right]

    # 추출한 영상을 서버 내에 저장한다.
    cv2.imwrite(settings.MEDIA_ROOT+'/'+name+'/'+name+'_4.jpg',tempImg)

def extractNose(img,l,name):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(28,36):
        x = l.part(i).x
        y = l.part(i).y
        if x < img.shape[1]:
            locX.append(x)
        if y < img.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)
    bottom = max(locY)+5
    left = min(locX)
    left = left-15 if left-15 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < img.shape[1] else img.shape[0]-1
   
    # 코를 추출한다.
    tempImg = img[top:bottom,left:right]

    # 추출한 영상을 서버 내에 저장한다.
    cv2.imwrite(settings.MEDIA_ROOT+'/'+name+'/'+name+'_3.jpg',tempImg)

def extractEyebrows(img,l,name):
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(17,26):
        x = l.part(i).x
        y = l.part(i).y
        if x < img.shape[1]:
            locX.append(x)
        if y < img.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)
  
    # 좌표들 중 가장자리인 것들을 구한다.
    top = min(locY)
    top = top-5 if top-5 > 0 else 0
    bottom = max(locY)+5
    left = min(locX)
    left = left-5 if left-5 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < img.shape[1] else img.shape[0]-1

    # 눈썹을 추출한다.
    tempImg = img[top:bottom,left:right]

    # 추출한 영상을 서버 내에 저장한다.
    cv2.imwrite(settings.MEDIA_ROOT+'/'+name+'/'+name+'_1.jpg',tempImg)
    
def extractEyes(img,l,name):    
    # 좌표를 저장할 리스트를 선언한다.
    locX = []
    locY = []

    # 좌측 눈부터 우측 눈 까지 (36 ~ 48) 좌표들을 종합한다.
    for i in range(36,48):
        x = l.part(i).x
        y = l.part(i).y
        if x < img.shape[1]:
            locX.append(x)
        if y < img.shape[0]:
            locY.append(y)
        #faceImg = cv2.circle(faceImg,(x,y),2,(0,255,0),-1)

    # 가장 가장자리인 영역들을 추출한다.
    top = min(locY)
    top = top-5 if top-5 > 0 else 0
    bottom = max(locY)+5
    left = min(locX)
    left = left-15 if left-15 > 0 else 0
    right = max(locX)
    right = right+15 if right+15 < img.shape[1] else img.shape[0]-1

    # 눈을 추출한다.
    tempImg = img[top:bottom,left:right]
    
    # 추출한 영상을 서버 내에 저장한다.    
    cv2.imwrite(settings.MEDIA_ROOT+'/'+name+'/'+name+'_2.jpg',tempImg)

def splitFace(name):    
    # 얼굴 인식용 클래스 생성
    face_detector = dlib.get_frontal_face_detector()

    # 랜드마크 클래스 생성
    face_pose_detector = dlib.shape_predictor(predictor_path)

    # 얼굴 정렬 클래스 생성
    face_aligner = openface.AlignDlib(predictor_path)

    print(str("settings.MEDIA_ROOT=")+settings.MEDIA_ROOT)

    # 원 이미지 불러오기
    img = cv2.imread(settings.MEDIA_ROOT+"/"+name+"/"+name+"_origin.jpg", cv2.IMREAD_COLOR)

    # cv2.namedWindow("test")
    # cv2.imshow("test",img)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()

    # # 파일명을 출력
    # # print("Processing file: {}".format(img))
     
    # 얼굴 인식 시작
    # 두 번째 인자는 샘플링 값(클수록 오래 걸림)
    dets = face_detector(img, 1)
    
    # 얼굴 인식이 안될 경우 -1 을 반환
    if len(dets) == 0:
        return -1

    # 세 좌표가 같은 위치에 오도록 하여 정렬한다
    # 19, 24, 8 = 왼쪽 눈썹, 오른쪽 눈썹, 가운데 턱  
    faceImg = face_aligner.align(200,img,dets[0],landmarkIndices=[19,24,33])

    # 정렬된 영상으로 다시 얼굴을 인식하여 랜드마크를 생성한다.
    d = face_detector(faceImg,1)

    # 얼굴 인식이 안될 경우 -1 을 반환
    if len(d) == 0:
        return -1
    l = face_pose_detector(faceImg,d[0])

    extractEyebrows(faceImg,l,name)
    extractEyes(faceImg,l,name)
    extractNose(faceImg,l,name)
    extractMouse(faceImg,l,name)

def insertDB(name,type,dir):
    i = Image()
    i.name = name
    i.type = type
    i.dir = dir 
    i.save()

def drawDots(img,l,start,end):
    res_img = img.copy()

    for i in range(start,end+1):
        x = l.part(i).x
        y = l.part(i).y
        cv2.circle(res_img,(x,y),CIRCLE_SIZE,(0,255,0),-1)
     
    return res_img

def drawPoints(name):    
    print(str("dir=")+settings.BASE_DIR)

    # 얼굴 인식용 클래스 생성
    face_detector = dlib.get_frontal_face_detector()

    # 랜드마크 클래스 생성
    face_pose_detector = dlib.shape_predictor(predictor_path)

    # 원 이미지 불러오기
    img = cv2.imread(settings.MEDIA_ROOT+"/"+name+"/"+name+"_origin.jpg", cv2.IMREAD_COLOR)

    # 얼굴 인식 시작
    # 두 번째 인자는 샘플링 값(클수록 오래 걸림)
    dets = face_detector(img, 1)
    
    # 얼굴 인식이 안될 경우 -1 을 반환
    if len(dets) == 0:
        return -1

    # 얼굴 내의 좌표를 감지한다.
    l = face_pose_detector(img,dets[0])

    # 원이미지를 복사하여 눈썹의 좌표를 찍는다. 후에 DB에 저장.
    eyebrow_img = drawDots(img,l,17,26)

    # 추출한 영상을 서버 내에 저장한다.
    cv2.imwrite(settings.MEDIA_ROOT+"/"+name+"/"+name+"_eyebrow.jpg",eyebrow_img)
    
    # 관련 정보를 DB에 저장한다.
    insertDB(name,"EYEBROW",settings.MEDIA_ROOT+"/"+name+"/"+name+"_eyebrow.jpg")

    # 눈
    eye_img = drawDots(img,l,36,47)
    cv2.imwrite(settings.MEDIA_ROOT+"/"+name+"/"+name+"_eye.jpg",eye_img)
    insertDB(name,"EYE",settings.MEDIA_ROOT+"/"+name+"/"+name+"_eye.jpg")

    # 코
    nose_img = drawDots(img,l,28,35)
    cv2.imwrite(settings.MEDIA_ROOT+"/"+name+"/"+name+"_nose.jpg",nose_img)
    insertDB(name,"NOSE",settings.MEDIA_ROOT+"/"+name+"/"+name+"_nose.jpg")

    # 입
    mouse_img = drawDots(img,l,48,67)
    cv2.imwrite(settings.MEDIA_ROOT+"/"+name+"/"+name+"_mouse.jpg",mouse_img)
    insertDB(name,"MOUSE",settings.MEDIA_ROOT+"/"+name+"/"+name+"_mouse.jpg")

    # 전체
    face_img = drawDots(img,l,17,67)
    cv2.imwrite(settings.MEDIA_ROOT+"/"+name+"/"+name+"_face.jpg",face_img)
    insertDB(name,"FACE",settings.MEDIA_ROOT+"/"+name+"/"+name+"_face.jpg")
    
