from django.urls import path
from . import views


app_name = 'travel'


urlpatterns = [
    path('list/', views.travel_lis, name='list'),
    path('create/', views.travel_create, name='create'),
    path('detail/<int:travel_id>/', views.travel_detail, name='detail'),
    path('delete/<int:travel_id>/', views.travel_delete, name='delete'),
    path('update/<int:travel_id>/', views.travel_update, name='update')
]