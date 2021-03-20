import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from results.figures.gapminder import Gapminder
from results.figures.rating_distribution import RatingDistribution
from results.models import SurveyResult

logger = logging.getLogger(__name__)


class Results(TemplateView):
    template_name = "results/results.html"

    def get_context_data(self, **kwargs):
        return {
            'rating_dist': RatingDistribution.get_html(),
            'gapminder': Gapminder.get_html()
        }

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        result = SurveyResult.objects.create(result=submission)
        result.save()
        return HttpResponse()
