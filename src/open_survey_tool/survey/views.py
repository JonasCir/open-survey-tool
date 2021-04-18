from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from open_survey_tool.utils.logger import get_logger
from survey.models import Surveys

logger = get_logger()


class Survey(TemplateView):
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        return {}


class SurveyContent(View):
    def get(self, request):
        logger.info('sending out survey')

        content = Surveys.objects.filter(name="First Survey").first().content_json
        return JsonResponse(content)
