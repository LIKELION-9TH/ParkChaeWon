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
    path('create/',views.create,name='create'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('edit/<str:id>',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
] 