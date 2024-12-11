from django.urls import path
from . import views


app_name = 'sports'


urlpatterns = [
    path('list/', views.sport_lis, name='list'),
    path('create/', views.sport_create, name='create'),
    path('detail/<int:sport_id>/', views.sport_detail, name='detail'),
    path('delete/<int:sport_id>/', views.sport_delete, name='delete'),
    path('update/<int:sport_id>/', views.sport_update, name='update')
]