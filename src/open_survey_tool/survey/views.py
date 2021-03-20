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

#class SurveyContent(View):
 #   return JsonResponse()