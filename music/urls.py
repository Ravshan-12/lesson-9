from django.urls import path
from . import views


app_name = 'music'


urlpatterns = [
    path('list/', views.music_lis, name='list'),
    path('create/', views.music_create, name='create'),
    path('detail/<int:music_id>/', views.music_detail, name='detail'),
    path('delete/<int:music_id>/', views.music_delete, name='delete'),
    path('update/<int:music_id>/', views.music_update, name='update')
]