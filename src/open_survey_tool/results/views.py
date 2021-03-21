import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from results.figures.base import Figure
from results.figures.gapminder import Gapminder
from results.figures.rating_distribution import RatingDistribution
from results.models import SurveyResult

logger = logging.getLogger(__name__)

cfg = Figure.html_config


class Results(TemplateView):
    template_name = "results/results.html"

    def get_context_data(self, **kwargs):
        print("CDF", cdf)
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
            'rating_5_2': RatingDistribution.get_html(cfg, "question5-2"),
            'gapminder': Gapminder.get_html(cfg)
        }

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        # todo does not check if all JSON keys are set
        result = SurveyResult.objects.create(result=submission)
        result.save()
        return HttpResponse()
