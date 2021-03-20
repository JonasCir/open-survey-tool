import logging

from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

# todo logger not working
logger = logging.getLogger(__name__)


class Survey(TemplateView):
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        return {}


class SurveyContent(View):
    def get(self, request):
        content = {
            'questions': [
                {
                    'type': "rating",
                    'name': "satisfaction",
                    'title': "How satisfied are you with the Product?",
                    'minRateDescription': "Not Satisfied",
                    'maxRateDescription': "Completely satisfied"
                }
            ]
        }
        return JsonResponse(content)
