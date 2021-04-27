import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from results.figures.general_box_chart import GeneralBoxChart
from results.figures.general_bubble import GeneralBubble
from results.figures.heat_map import HeatMap
from results.figures.pie_chart import PieChart
from results.figures.scatter_matrix import ScatterMatrix
from results.models import SurveyResponses
from results.utils.figure import Figure
from results.utils.rating_distribution import RatingDistribution
from survey.models import Surveys

logger = logging.getLogger(__name__)

cfg = Figure.html_config


class Results(TemplateView):
    template_name = "results/results.html"

    @staticmethod
    def create_context_data():
        # todo still a little bit hacky but shows the idea and works quite nice
        study_config = Surveys.objects.first().definition_json['questions']
        res = list()
        for elem in study_config:
            if elem['type'] == 'html':
                res.append(elem['html'])
            else:
                # todo there is a special place in hell for this...
                res.append(f"<h2>{elem['title']}</h2>")
                res.append(RatingDistribution.get_html(cfg, elem['name']))

        return {
            'results': res
        }

    def get_context_data(self, **kwargs):
        return Results.create_context_data()

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        # todo does not check if all JSON keys are set
        result = SurveyResponses.objects.create(response=submission)
        result.save()
        return HttpResponse()


class InternalResults(TemplateView):
    template_name = 'results/internalresults.html'

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
            'box_vertrauen': GeneralBoxChart.get_html(cfg, 'Vertrauen')
        }
