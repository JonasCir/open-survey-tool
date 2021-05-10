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
        return {"pk": kwargs["pk"]}


class SurveyOverviewSingle(TemplateView):
    """
    This page shows a survey to the user.
    """
    template_name = "survey/index.html"

    def get_context_data(self, **kwargs):
        overviewData = Surveys.objects.filter(
            pk=kwargs["pk"]).first().definition_json['overview']
        return {"time": overviewData["time"], "description": overviewData["description"], "contact": overviewData["contact"], "duration": overviewData["duration"], "title": overviewData["title"], "img": "img/"+overviewData["img"], "pk": kwargs["pk"]}


class SurveyOverviewAll(TemplateView):
    """
    This page shows a survey to the user.
    """
    template_name = "survey/all.html"

    def get_context_data(self, **kwargs):
        overviewData = Surveys.objects.order_by('pk').values()
        res = list()
        for elem in overviewData:
            res.append({"time": elem["definition_json"]["overview"]["time"], "duration": elem["definition_json"]["overview"]["duration"],
                       "title": elem["definition_json"]["overview"]["title"], "img": "img/"+elem["definition_json"]["overview"]["img"], "pk": elem["id"]})
        return {'surveys': res}


class SurveyList(ListCreateAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer


class SurveyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer
