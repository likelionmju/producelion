from django.urls import path
from . import views
    
urlpatterns = [
    path('',views.result,name='result'),
    path('before',views.beforeteam,name='beforeteam'),
]
