from django.http import Http404
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
        survey = Surveys.objects.filter(uuid=kwargs['survey_id']).first()
        if survey is not None:
            return {"survey_id": kwargs["survey_id"]}
        else:
            raise Http404("Questions for this survey are not available.")


class SurveyOverviewDetails(TemplateView):
    """
    This page shows a survey to the user.
    """
    template_name = "survey/index.html"

    def get_context_data(self, **kwargs):
        survey = Surveys.objects.filter(uuid=kwargs['survey_id']).first()

        if survey is not None:
            overview_data = survey.definition_json['overview']
        else:
            raise Http404("Details for this survey are not available.")

        overview_data['survey_id'] = kwargs['survey_id']
        overview_data['img'] = 'img/' + overview_data['img']
        return overview_data


class SurveyOverviewAll(TemplateView):
    """
    This page shows a survey to the user.
    """
    template_name = "survey/all.html"

    def get_context_data(self, **kwargs):
        overview_data = Surveys.objects.order_by('uuid').values()
        # todo show something like "Aktuell gibt es keine Umfragen" if overview data is empty
        res = list()
        for elem in overview_data:
            overview = elem["definition_json"]["overview"]
            res.append({
                "time": overview["time"],
                "duration": overview["duration"],
                "title": overview["title"],
                "img": "img/" + overview["img"],
                "survey_id": elem["uuid"]
            })
        return {'surveys': res}


class SurveyList(ListCreateAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer
    lookup_url_kwarg = 'survey_id'


class SurveyDetails(RetrieveUpdateDestroyAPIView):
    queryset = Surveys.objects.all()
    serializer_class = SurveySerializer
    lookup_url_kwarg = 'survey_id'
