from django.contrib import admin
from .models import Eye, Eye_Brow, Nose, Mouse, Image


# Register your models here.
admin.site.register(Image)

admin.site.register(Eye_Brow)
admin.site.register(Eye)
admin.site.register(Nose)
admin.site.register(Mouse)
