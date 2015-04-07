from rest_framework import generics

from .models import About, Education, Experience, Skill
from .serializers import AboutSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer


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
