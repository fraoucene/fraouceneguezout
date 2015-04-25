from rest_framework import serializers

from .models import About, ConfigurationColor, ConfigurationTitle, Education, Experience, Skill, TitleConfiguration


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('pk', 'title','title_fr', 'body','body_fr')


class TitleConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TitleConfiguration
        fields = ('pk', 'title', 'label_fr', 'label_en', 'subtitle_fr', 'subtitle_en')

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
        fields = ('pk', 'school', 'description', 'description_fr', 'start_on', 'end_on', 'current', 'title',
                   'title_fr', 'tools', 'location', 'detail', 'detail_fr', 'lien')


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ('pk', 'company','start_on', 'end_on', 'description', 'description_fr', 'current', 'title',
                    'title_fr', 'tools', 'location', 'detail', 'detail_fr', 'lien')


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('pk', 'label', 'description', 'grade', 'row',)
