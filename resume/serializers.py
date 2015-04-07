from rest_framework import serializers

from .models import About, ConfigurationColor, ConfigurationTitle, Education, Experience, Skill


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('pk', 'title', 'body',)



class ConfigurationColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigurationColor
        fields = (
            'pk', 'label', 'active',
            'title', 'subtitle', 'about', 'skills', 'experiences', 'education',
        )


class ConfigurationTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigurationTitle
        fields = (
            'pk', 'label', 'active',
            'title', 'subtitle', 'about', 'skills', 'experiences', 'education',
        )



class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ('pk', 'school', 'description', 'start_on', 'end_on', 'current', 'title', 'tools', 'location', 'detail', 'lien')


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ('pk', 'company','start_on', 'end_on', 'description', 'current', 'title', 'tools', 'location', 'detail', 'lien')


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('pk', 'label', 'description', 'grade', 'row',)
