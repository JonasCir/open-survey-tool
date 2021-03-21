from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from open_survey_tool.utils.logger import get_logger

logger = get_logger()


class Survey(TemplateView):
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        return {}


class SurveyContent(View):
    def get(self, request):
        logger.info('sending out survey')

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
