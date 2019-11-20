from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.conf import settings
from . import sql, detector
from datetime import date
from .models import Image, Eye, Eye_Brow, Nose, Mouse
from .serializers import EyeSerializer, Eye_BrowSerializer, NoseSerializer, MouseSerializer, ImageSerializer
from django.core.files.storage import default_storage
from . import Images_Classification_Eyebrow256 as md_eyebrow
from . import Images_Classification_Eye256 as md_eye
from . import Images_Classification_Nose256 as md_nose
from . import Images_Classification_Mouse256 as md_mouse
from threading import Timer

import json, os, cv2, time, random, shutil

@api_view(['POST', 'GET'])
def faces(request) :
    if request.method == 'POST' :
        # db 객체 생성
        image = Image()

        # getfile
        file = request.FILES['image']

        # image name
        while True :
            name = str(random.uniform(1,10))
            temp = Image.objects.filter(name = name)
            
            if temp != None :
                image.name = name
                break

        #file name
        file.name = image.name+'_origin.jpg'

        # image dir
        image.dir = os.path.join(settings.MEDIA_ROOT) + '/' + image.name

        # image type
        image.type = 'ORIGIN'

        # 폴더 생성
        try:
            if (os.path.isdir(image.name)) :
                os.remove(image.dir)
            
            os.makedirs(image.dir)
            print(image.dir)
            
            # 폴더 이름 저장
            folder_name = image.name

            # 파일 저장
            default_storage.save(folder_name+'/'+image.name+'_origin.jpg', file)
            
            # 점이 찍인 영상 5개 생성 및 저장
            if detector.splitFace(name) == -1:
                return Response("split_fail")
                
            # 가중치에 비교할 이목구비 부분영상 추출 및 저장(DB x)
            if detector.drawPoints(name) == -1:
                return Response("draw_fail")

            eyebrow_result = md_eyebrow.evaluate(image.name)
            eye_result = md_eye.evaluate(image.name)
            nose_result = md_nose.evaluate(image.name)
            mouse_result = md_mouse.evaluate(image.name)
        except OSError as e:
            print(e)

        # image db 저장
        image.save()

        # db numberslist
        numbers = [eyebrow_result,eye_result,nose_result,mouse_result]
        
        # db 가져오기
        data = sql.db_return(numbers, image.name)
        
        def timer_delete() :
            print("5분 지남")
            data = Image.objects.filter(name = image.name)
            path = os.path.join(settings.MEDIA_ROOT) + '/' + name
            shutil.rmtree(path, ignore_errors=True)
            data.delete()

        Timer(300, timer_delete).start()
        
        
        return JsonResponse(data, json_dumps_params = {'ensure_ascii': True}, safe = True)
    elif request.method == "GET" :
        # db 지우기 함수 실행
        print("delete")
        name = request.GET.get('name')
        print(name)
        result = sql.db_delete(name)

        # 날짜와 다른 data 가져오기
        # datas = Image.objects.exclude(name = name)
        # datas = ImageSerializer(datas, many = True)

        # for data in datas :
        #     data.delete()
        
        return Response(result, status=status.HTTP_200_OK)

@api_view(['GET'])
def dictionary(request) :
    if request.method == "GET" :

        # types = [EYE_BROW, EYE, NOSE, MOUSE]
        types = request.GET.get('types')

        data = sql.db_dictionarys(types)

        return Response(data, status=status.HTTP_200_OK)

    return Response(None, status=status.HTTP_404_NOT_FOUND)
