import logging

from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from responses.figures.general_box_chart import GeneralBoxChart
from responses.figures.general_bubble import GeneralBubble
from responses.figures.heat_map import HeatMap
from responses.figures.pie_chart import PieChart
from responses.figures.scatter_matrix import ScatterMatrix
from responses.models import SurveyResponses
from responses.serializers import SurveyResponseSerializer
from responses.utils.figure import Figure
from responses.utils.rating_distribution import RatingDistribution
from surveys.models import Surveys

logger = logging.getLogger(__name__)

cfg = Figure.html_config


class SurveyResponse(TemplateView):
    """
    This page shows all responses to the survey to the user.
    """
    template_name = "responses/survey_result.html"

    @staticmethod
    def create_context_data(self, kwargs):
        # todo still a little bit hacky but shows the idea and works quite nice
        study_config = Surveys.objects.filter(
            id=kwargs["pk"]).first().definition_json['questions']
        res = list()
        for elem in study_config:
            if elem['type'] == 'html':
                res.append(elem['html'])
            else:
                # todo there is a special place in hell for this...
                res.append(f"<h2>{elem['title']}</h2>")
                res.append(RatingDistribution.get_html(cfg, elem['name']))

        return {'results': res, 'pk': kwargs["pk"]}

    def get_context_data(self, **kwargs):
        return SurveyResponse.create_context_data(self, kwargs)


class ResponseList(ListCreateAPIView):
    queryset = SurveyResponses.objects.all()
    serializer_class = SurveyResponseSerializer


class ResponseDetail(RetrieveUpdateDestroyAPIView):
    queryset = SurveyResponses.objects.all()
    serializer_class = SurveyResponseSerializer


class InternalResults(TemplateView):
    template_name = 'responses/internalresults.html'

    def get_context_data(self, **kwargs):
        return {
            'bubbles_users': GeneralBubble.get_html(cfg, y_axis_question='question1_1', x_axis_question='question1_2'),
            'box_all': GeneralBoxChart.get_html(cfg),
            'scatter_matrix': ScatterMatrix.get_html(cfg),
            'pie_chart': PieChart.get_html(cfg),
            'heat_map': HeatMap.get_html(cfg),
            'box_verhalten': GeneralBoxChart.get_html(cfg, 'Verhalten'),
            'box_kompetenz': GeneralBoxChart.get_html(cfg, 'Kompetenz'),
            'box_information': GeneralBoxChart.get_html(cfg, 'Information'),
            'box_vertrauen': GeneralBoxChart.get_html(cfg, 'Vertrauen'),
            'pk': kwargs["pk"]
        }
