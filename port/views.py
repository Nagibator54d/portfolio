from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Profile, Skill, Project, Experience, Education
from rest_framework import generics

# class ProfileListView(ListView):
#     model = Profile
#     template_name = 'profile_list.html'


def profile_detail(request,pk):
    profile=Profile.objects.get(id=pk )
    context={
        'profile':profile,
    }
    return render(request,'profile_detail.html', context)

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations
    })

def skill(request,pk):
    skills=Skill.objects.get(id=pk)
    context={
        'skills':skills,
    }
    return render(request,'skill.html', context)


def project(request,pk):
    projects=Project.objects.get(id=pk )
    context={
        'projects':projects,
    }
    return render(request,'project.html', context)


def experience(request,pk):
    experiences=Experience.objects.get(id=pk )
    context={
        'experiences':experiences,
    }
    return render(request,'experience.html', context)




def education(request,pk):
    educations=Education.objects.get(id=pk )
    context={
        'educations':educations,
    }
    return render(request,'education.html', context)


