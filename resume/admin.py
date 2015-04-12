
from django.contrib import admin

from resume.models import *


class ConfigurationTitleAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pk', 'label', 'active', 'title', 'subtitle',)
    list_editable = ('label', 'active', 'title', 'subtitle',)
    list_filter = ()
    search_fields = ('label',)

class TitleConfigurationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pk', 'title', 'label_fr', 'label_en', 'subtitle_fr', 'subtitle_en')
    list_editable = ('title', 'label_fr', 'label_en', 'subtitle_fr', 'subtitle_en')
    list_filter = ()
    search_fields = ('title',)

class ConfigurationColorAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pk', 'label', 'active', 'title', 'subtitle',)
    list_editable = ('label', 'active', 'title', 'subtitle',)
    list_filter = ()
    search_fields = ('label',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pk', 'title',)
    list_editable = ('title',)
    list_filter = ()
    search_fields = ('title',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pk', 'label', 'description', 'grade', 'row', )
    list_editable = ('label', 'description', 'grade', 'row',)
    list_filter = ('grade', 'row',)
    search_fields = ('label', 'description',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'pk',
        'company', 'description', 'start_on', 'end_on', 'current','title', 'tools', 'location', 'detail', 'lien',
    )
    list_editable = ('company', 'description', 'start_on', 'end_on', 'current','title', 'tools', 'location', 'detail', 'lien',)
    list_filter = ('start_on', 'end_on', 'current',)
    search_fields = ('company', 'description',)

class EducationAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'pk',
        'school', 'description', 'start_on', 'end_on', 'current', 'title', 'tools', 'location', 'detail', 'lien',
    )
    list_editable = ('school', 'description', 'start_on', 'end_on', 'current' ,'title', 'tools', 'location', 'detail', 'lien',)
    list_filter = ('start_on', 'end_on', 'current',)
    search_fields = ('school', 'description',)


admin.site.register(ConfigurationTitle, ConfigurationTitleAdmin)
admin.site.register(TitleConfiguration, TitleConfigurationAdmin)
admin.site.register(ConfigurationColor, ConfigurationColorAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
