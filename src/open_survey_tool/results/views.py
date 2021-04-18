import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from results.internal.figures.generalBoxChart import GeneralBoxChart
from results.internal.figures.generalBubble import GeneralBubble
from results.internal.figures.heatMap import HeatMap
from results.internal.figures.pieChart import PieChart
from results.internal.figures.scatterMatrix import ScatterMatrix
from results.models import SurveyResult
from results.utils.figure import Figure
from results.utils.rating_distribution import RatingDistribution

logger = logging.getLogger(__name__)

cfg = Figure.html_config


class Results(TemplateView):
    template_name = "results/results.html"

    def get_context_data(self, **kwargs):
        return {
            'rating_1_1': RatingDistribution.get_html(cfg, "question1-1"),
            'rating_1_2': RatingDistribution.get_html(cfg, "question1-2"),
            'rating_2_1': RatingDistribution.get_html(cfg, "question2-1"),
            'rating_2_2': RatingDistribution.get_html(cfg, "question2-2"),
            'rating_3_1': RatingDistribution.get_html(cfg, "question3-1"),
            'rating_3_2': RatingDistribution.get_html(cfg, "question3-2"),
            'rating_4_1': RatingDistribution.get_html(cfg, "question4-1"),
            'rating_4_2': RatingDistribution.get_html(cfg, "question4-2"),
            'rating_5_1': RatingDistribution.get_html(cfg, "question5-1"),
            'rating_5_2': RatingDistribution.get_html(cfg, "question5-2")
        }

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        # todo does not check if all JSON keys are set
        result = SurveyResult.objects.create(result=submission)
        result.save()
        return HttpResponse()


class InternalResults(TemplateView):
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
