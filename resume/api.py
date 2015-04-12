from rest_framework import generics

from .models import About, Education, Experience, Skill, TitleConfiguration
from .serializers import AboutSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, TitleConfigurationSerializer


class TitleConfigurationList(generics.ListAPIView):
    queryset = TitleConfiguration.objects.order_by('-pk')
    serializer_class = TitleConfigurationSerializer
    paginate_by = None

class AboutList(generics.ListAPIView):
    queryset = About.objects.order_by('-pk')
    serializer_class = AboutSerializer
    paginate_by = None


class EducationList(generics.ListAPIView):
    queryset = Education.objects.order_by('-pk')
    serializer_class = EducationSerializer
    paginate_by = None


class ExperienceList(generics.ListAPIView):
    queryset = Experience.objects.order_by('-pk')
    serializer_class = ExperienceSerializer
    paginate_by = None


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all().order_by('-pk')   
    serializer_class = SkillSerializer
    paginate_by = 100
