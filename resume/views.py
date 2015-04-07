from django.http import JsonResponse

from .models import ConfigurationColor, ConfigurationTitle
from .serializers import ConfigurationColorSerializer, ConfigurationTitleSerializer


def configuration(request):
    if request.method == 'GET':
        try:
            configuration_title = ConfigurationTitle.objects.get(active=True)
            titles = ConfigurationTitleSerializer(configuration_title).data
        except (ConfigurationTitle.DoesNotExist, ConfigurationTitle.MultipleObjectsReturned):
            titles = {}
        try:
            configuration_color = ConfigurationColor.objects.get(active=True)
            colors = ConfigurationColorSerializer(configuration_color).data
        except (ConfigurationColor.DoesNotExist, ConfigurationColor.MultipleObjectsReturned):
            colors = {}
        response = {'titles': titles, 'colors': colors}
        return JsonResponse(response)
