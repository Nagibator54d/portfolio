from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='profile_list'),
    path('profile/<int:pk>/',profile_detail , name='profile_detail'),
    path('skill/new/', skill, name='skill'),
    path('project/new/', project, name='project'),
    path('experience/new/', experience, name='experience'),
    path('education/new/', education, name='education'),
]
