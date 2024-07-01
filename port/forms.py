# portfolio/forms.py

from django import forms
from .models import Profile, Project, Skill, Experience, Education

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','bio', 'profile_picture', 'contact_email', ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['profile','title', 'description', 'image', 'link']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['profile','name', 'proficiency']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['profile','title','company',  'start_date', 'end_date', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['profile','school', 'degree',  'start_date', 'end_date', 'description']

class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
