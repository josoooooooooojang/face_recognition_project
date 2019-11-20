from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('faces/', views.faces),
    path('dictionarys/', views.dictionary),
    # path('DB_delete/', views.face_delete)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)