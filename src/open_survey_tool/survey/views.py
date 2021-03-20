from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class Index(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")


class Survey(TemplateView):
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return {}
