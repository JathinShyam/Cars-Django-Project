from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('update/', views.update),
    path('enter/', views.enter),
    path('display/', views.display),
    path('importdata/', views.importData),
    path('updatefile/', views.updateFile),
    path('delete/', views.delete),
    path('sendemail/', views.mailing),
]
