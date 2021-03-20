import json
import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class Results(TemplateView):
    template_name = "results/results.html"

    def get_context_data(self, **kwargs):
        return {}

    def post(self, request):
        submission = json.loads(request.POST.get('submission'))
        print(submission)
        return HttpResponse()
