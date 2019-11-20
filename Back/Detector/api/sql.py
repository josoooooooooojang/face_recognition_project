from .models import Eye, Eye_Brow, Mouse, Nose, Image
from .serializers import NoseSerializer, EyeSerializer, Eye_BrowSerializer, MouseSerializer, ImageSerializer
import os, shutil
from django.conf import settings

# persons = Person.objects.filter(first_name = first)
def db_return(numbers, name) :

    eye_brow = Eye_Brow()
    eye = Eye()
    nose = Nose()
    mouse = Mouse()
    
    eye_brow = Eye_Brow.objects.filter(number = numbers[0][0])
    eye = Eye.objects.filter(number = numbers[1][0])
    nose = Nose.objects.filter(number = numbers[2][0])
    mouse = Mouse.objects.filter(number = numbers[3][0])
    
    noseserializer = NoseSerializer(nose, many = True)
    eyeserializer = EyeSerializer(eye, many = True)
    eye_browserializer = Eye_BrowSerializer(eye_brow, many = True)
    mouseserializer = MouseSerializer(mouse, many = True)

    data = {
        'name' : name,
        'eye_brow' : eye_browserializer.data,        
        'eye' : eyeserializer.data,
        'nose' : noseserializer.data,
        'mouse' : mouseserializer.data,
    }
    
    return data

def db_delete(name) :
    data = Image.objects.filter(name = name)
    path = os.path.join(settings.MEDIA_ROOT) + '/' + name
    shutil.rmtree(path, ignore_errors=True)
    data.delete()

    return 'OK'

def db_dictionarys(types) :
    if types == "EYEBROW" :
        eye_brows = Eye_Brow.objects.all()
        serializer = Eye_BrowSerializer(eye_brows, many = True)
        return serializer.data

    elif types == "EYE" :
        eyes = Eye.objects.all()
        serializer = EyeSerializer(eyes, many = True)
        return serializer.data

    elif types == "NOSE" :
        noses = Nose.objects.all()
        serializer = NoseSerializer(noses, many = True)
        return serializer.data

    elif types == "MOUSE" :
        mouses = Mouse.objects.all()
        serializer = MouseSerializer(mouses, many = True)
        return serializer.data