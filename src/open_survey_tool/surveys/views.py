from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from open_survey_tool.utils.logger import get_logger
from surveys.models import Surveys
from surveys.serializers import SurveySerializer

logger = get_logger()


class Survey(TemplateView):
    """
    This page shows a survey to the user.
    """
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        return {}


class SurveyList(ListCreateAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer


class SurveyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer
