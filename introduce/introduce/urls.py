from django.contrib import admin
from django.urls import path
from chaewon import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('hobby/',views.hobby,name='hobby'),
    path('music/',views.music,name='music'),
    path('photo',views.photo,name='photo'),
    path('place/',views.place,name='place'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
