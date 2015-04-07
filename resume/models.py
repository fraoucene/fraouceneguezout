#from dateutil import relativedelta
import datetime
from django.db import models


class ConfigurationTitle(models.Model):
    """Store configuration for titles.
    """

    label = models.CharField('Label', max_length=255, unique=True, default='Default')
    active = models.BooleanField('Active', default=True)
    title = models.CharField('Title', max_length=255)
    subtitle = models.CharField('Subtitle', max_length=255)
    about = models.CharField('About title', max_length=255, null=True, blank=True)
    skills = models.CharField('Skills title', max_length=255)
    experiences = models.CharField('Experiences title', max_length=255)
    education = models.CharField('Education title', max_length=255)

    def __unicode__(self):
        return self.label


class ConfigurationColor(models.Model):
    """Store configuration for colors.
    """

    label = models.CharField('Label', max_length=255, unique=True, default='Default')
    active = models.BooleanField('Active', default=True)
    title = models.CharField('Title', max_length=7, default='#FFFFFF')
    subtitle = models.CharField('Subtitle', max_length=7, default='#FFFFFF')
    about = models.CharField('About title', max_length=7, default='#FFFFFF')
    skills = models.CharField('Skills title', max_length=7, default='#FFFFFF')
    experiences = models.CharField('Experiences title', max_length=7, default='#FFFFFF')
    education = models.CharField('Education title', max_length=7, default='#FFFFFF')

    def __unicode__(self):
        return self.label



class About(models.Model):
    """Store data for about section.
    """

    title = models.CharField('Title', max_length=255)
    body = models.TextField('Body', null=True, blank=True)

    def __unicode__(self):
        return self.title



class Skill(models.Model):
    """Store data for skills section.
    """

    ROW_CHOICES = (
        (1, 'Skills'),
        (2, 'Tools'),
        (3, 'Langages'),
    )

    label = models.CharField('Skill', max_length=255, )
    description = models.TextField('Description', null=True, blank=True)
    grade = models.PositiveIntegerField('Grade', default=100)
    row = models.PositiveIntegerField('Row', choices=ROW_CHOICES, default=ROW_CHOICES[0][0])

    def __unicode__(self):
        return self.label

class Experience(models.Model):
    """Store data for experiences section.
    """

    company = models.CharField('Company', max_length=255)
    start_on = models.DateField('Start on')
    end_on =  models.DateField('End on', blank=True, null=True)
    current = models.BooleanField('Current', default=False)
    description = models.TextField('Description', blank=True, null=True)
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    tools = models.TextField('Tools', blank=True, null=True)
    location = models.TextField('Location', blank=True, null=True)
    detail = models.TextField('Detail', blank=True, null=True)
    lien = models.CharField('Lien', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.company


class Education(models.Model):
    """Store data for education section.
    """

    school = models.CharField('School', max_length=255)
    start_on = models.DateField('Start on')
    end_on =  models.DateField('End on', blank=True, null=True)
    current = models.BooleanField('Current', default=False)
    description = models.TextField('Description', blank=True, null=True)
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    tools = models.TextField('Tools', blank=True, null=True)
    location = models.TextField('Location', blank=True, null=True)
    detail = models.TextField('Detail', blank=True, null=True)
    lien = models.CharField('Lien', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.school
