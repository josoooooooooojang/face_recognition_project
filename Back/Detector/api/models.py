from django.db import models
import os
from django.conf import settings
from datetime import date  

# Create your models here.

class Image(models.Model) :
    name = models.CharField(null = False , blank = False, max_length = 20)

    # type = [FACE, EYEBROW, EYE, NOSE, MOUSE, ORIGIN]
    type = models.CharField(null = False, blank = False, max_length = 20)
    dir = models.TextField(null = False, blank = False, max_length = 255)
    create_at = models.DateField(default=date.today, blank = False)
    
    def __str__(self) :
        return self.name + ':' + self.type
        
    # def fileremove(self) :
    #     print(self.img.name+"파일을 지우겠습니다.")
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.name))

class Eye_Brow(models.Model) :
    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 15)
    positive = models.TextField(max_length = 255)
    negative = models.TextField(max_length = 255)
    
    def __str__(self) :
        return str(self.number)

class Eye(models.Model) :
    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 15)
    positive = models.TextField(max_length = 255)
    negative = models.TextField(max_length = 255)

    def __str__(self) :
        return str(self.number)

class Nose(models.Model) :
    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 15)
    positive = models.TextField(max_length = 500)
    negative = models.TextField(max_length = 500)

    def __str__(self) :
        return str(self.number)
        
class Mouse(models.Model) :
    number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 15)
    positive = models.TextField(max_length = 255)
    negative = models.TextField(max_length = 255)

    def __str__(self) :
        return str(self.number)