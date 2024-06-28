from rest_framework import serializers
from port.models import Profile,Project,Skill,Experience,Education


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields='__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=Project
        fields='__all__'

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model=Skill
        fields='__all__'

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Experience
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Education
        fields='__all__'