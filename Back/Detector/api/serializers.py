# from .models import Person
from rest_framework import serializers
from django.conf.urls import url, include
from .models import Nose, Mouse, Eye, Eye_Brow, Image

class NoseSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Nose
        fields = ('number', 'title', 'positive', 'negative')

class EyeSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Eye
        fields = ('number', 'title', 'positive', 'negative')

class MouseSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Mouse
        fields = ('number', 'title', 'positive', 'negative')

class Eye_BrowSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Eye_Brow
        fields = ('number', 'title', 'positive', 'negative')

class ImageSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Image
        fields = ('name', 'type', 'dir', 'create_at')


