from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .api import AboutList, EducationList, ExperienceList, SkillList, TitleConfigurationList


urlpatterns = patterns('resume.views',
    url(r'^about/$',          AboutList.as_view(),       name='about-list'),
    url(r'^configuration/$',  'configuration',           name='configuration'),
    url(r'^titles/$',          TitleConfigurationList.as_view(),       name='title-configuration-list'),
    url(r'^education/$',      EducationList.as_view(),   name='education'),
    url(r'^experiences/$',    ExperienceList.as_view(),  name='experience-list'),
    url(r'^skills/$',         SkillList.as_view(),       name='skill-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
