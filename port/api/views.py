from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from port.models import Profile,Project,Skill,Experience,Education
from .serializers import ProfileSerializer,ProjectSerializer,SkillSerializer,ExperienceSerializer,EducationSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import *
from django.shortcuts import get_object_or_404


class ProfileListView(GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,):

    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer           

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProfileDetailView(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)           
    
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)           

     
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           

class ProjectListView(GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,):

    queryset=Project.objects.all()
    serializer_class=ProjectSerializer           

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProjectDetailView(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)           
    
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)           

     
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           


class SkillListView(GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,):

    queryset=Skill.objects.all()
    serializer_class=SkillSerializer           

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SkillDetailView(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)           
    
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)           

     
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           


class ExperienceListView(GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,):

    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer           

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ExperienceDetailView(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)           
    
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)           

     
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           


class EducationListView(GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,):

    queryset=Education.objects.all()
    serializer_class=EducationSerializer           

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def create(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EducationDetailView(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset=Education.objects.all()
    serializer_class=EducationSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)           
    
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)           

     
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           

class ProfileViewSet(ViewSet):

    queryset=Profile.objects.all()

    def list(self,request):
       serializer=ProfileSerializer(self.queryset, many=True)

       return Response(serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, pk=None):
        profile=get_object_or_404(self.queryset, pk=pk)
        serializer= ProfileSerializer(profile)

        return Response(serializer.data, status=HTTP_200_OK)

    def create(self,request):
        serializer=ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    def update(self,request, pk=None):
        profile=get_object_or_404(self.queryset, pk=pk)
        serializer=ProfileSerializer(profile, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        profile=get_object_or_404(self.queryset, pk=pk)
        serializer=ProfileSerializer(profile,data=request.data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_403_FORBIDDEN )

    def destroy(self, request, pk=None):
        profile=get_object_or_404(self.queryset,pk=pk)
        profile.delete()
        return Response(status=HTTP_204_NO_CONTENT)    
        
