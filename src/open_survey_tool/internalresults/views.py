import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from internalresults.figures.base import Figure
from internalresults.figures.gapminder import Gapminder
from internalresults.figures.rating_distribution import RatingDistribution
from internalresults.figures.generalBubble import GeneralBubble
from internalresults.figures.generalBoxChart import GeneralBoxChart
from internalresults.figures.scatterMatrix import ScatterMatrix

from internalresults.figures.pieChart import PieChart
from internalresults.figures.heatMap import HeatMap

from internalresults.models import SurveyResult

logger = logging.getLogger(__name__)

cfg = Figure.html_config


class Results(TemplateView):
    template_name = "results/internalresults.html"

    def get_context_data(self, **kwargs):
        return {
            'bubbles_users': GeneralBubble.get_html(cfg, "question1-1"),
            'box_all': GeneralBoxChart.get_html(cfg),
            'scatter_matrix': ScatterMatrix.get_html(cfg),
            'pie_chart': PieChart.get_html(cfg),
            'heat_map': HeatMap.get_html(cfg),
            'box_verhalten': GeneralBoxChart.get_html(cfg, "Verhalten"),
            'box_kompetenz': GeneralBoxChart.get_html(cfg, "Kompetenz"),
            'box_information': GeneralBoxChart.get_html(cfg, "Information"),
            'box_vertrauen': GeneralBoxChart.get_html(cfg, "Vertrauen")
        }

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        # todo does not check if all JSON keys are set
        result = SurveyResult.objects.create(result=submission)
        result.save()
        return HttpResponse()
