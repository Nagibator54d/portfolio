from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Profile, Skill, Project, Experience, Education
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
    # if request.method =='POST':
    #     form=ContactForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         name=form.cleaned_data['name']
    #         email=form.cleaned_data['email']
    #         message=form.cleaned_data['message']

    #         html=render_to_string('templates/home.html',{
    #             'name': name,
    #             'email': email,
    #             'message': message,
    #         })


    #         print('The form is valid')

    #         send_mail('The contact form message','This is the message','noreply@codewithstein.com', ['hadhdon1@gmail.com'] ,html_message=html)

    #         return redirect('profile_list')
    # else:
    #     form = ContactForm()


    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'home.html', {
        # 'form':form,
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
    return render(request,'home.html', context)


def experience(request,pk):
    experiences=Experience.objects.get(id=pk )
    context={
        'experiences':experiences,
    }
    return render(request,'home.html', context)




def education(request,pk):
    educations=Education.objects.get(id=pk )
    context={
        'educations':educations,
    }
    return render(request,'home.html', context)


    