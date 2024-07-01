from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from.views import (ProfileListView,
                    ProfileDetailView,
                    ProjectListView,
ProjectDetailView,SkillListView,SkillDetailView,ExperienceListView,ExperienceDetailView,EducationListView,EducationDetailView
)
router=DefaultRouter()
router.register('profile/',ProfileViewSet, basename='profile' )


urlpatterns=[
    path('profiles/',ProfileListView.as_view(),name='profile_list'),
    path('<int:pk>/',ProfileDetailView.as_view(),name='profile_detail'),
    path('projects/',ProjectListView.as_view(),name='project_list'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='project_detail'),
    path('projects/',SkillListView.as_view(),name='skill_list'),
    path('project/<int:pk>/',SkillDetailView.as_view(),name='skill_detail'),
    path('projects/',ExperienceListView.as_view(),name='exp_list'),
    path('project/<int:pk>/',ExperienceDetailView.as_view(),name='exp_detail'),
    path('projects/',EducationListView.as_view(),name='education_list'),
    path('projects/<int:pk>/',EducationDetailView.as_view(),name='education_detail'),


]+router.urls