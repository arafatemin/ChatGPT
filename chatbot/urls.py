from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', chatbot, name='chat'),
    path('', index, name='index'),
]