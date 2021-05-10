from django.http import Http404
from django.views.generic import TemplateView

from results.utils.figure import Figure
from results.utils.rating_distribution import RatingDistribution
from surveys.models import Surveys

cfg = Figure.html_config


class SurveyResult(TemplateView):
    """
    This page shows all results to the survey to the user.
    """
    template_name = "responses/survey_result.html"

    @staticmethod
    def create_context_data(kwargs):
        # todo still a little bit hacky but shows the idea and works quite nice

        # get the survey and handle the case for 
        survey = Surveys.objects.filter(uuid=kwargs["survey_id"]).first()
        if survey is not None:
            study_config = survey.definition_json['questions']
        else:
            raise Http404("Results for this survey are not available.")

        res = list()
        for elem in study_config:
            if elem['type'] == 'html':
                res.append(elem['html'])
            else:
                # todo there is a special place in hell for this...
                res.append(f"<h2>{elem['title']}</h2>")
                res.append(RatingDistribution.get_html(cfg, elem['name']))

        return {'results': res, 'survey_id': kwargs["survey_id"]}

    def get_context_data(self, **kwargs):
        return SurveyResult.create_context_data(kwargs)

# class InternalResults(TemplateView):
#     template_name = 'responses/internalresults.html'
#
#     def get_context_data(self, **kwargs):
#         return {
#             'bubbles_users': GeneralBubble.get_html(cfg, y_axis_question='question1_1', x_axis_question='question1_2')
#             'box_all': GeneralBoxChart.get_html(cfg),
#             'scatter_matrix': ScatterMatrix.get_html(cfg),
#             'pie_chart': PieChart.get_html(cfg),
#             'heat_map': HeatMap.get_html(cfg),
#             'box_verhalten': GeneralBoxChart.get_html(cfg, 'Verhalten'),
#             'box_kompetenz': GeneralBoxChart.get_html(cfg, 'Kompetenz'),
#             'box_information': GeneralBoxChart.get_html(cfg, 'Information'),
#             'box_vertrauen': GeneralBoxChart.get_html(cfg, 'Vertrauen'),
#             'surveyid': kwargs["surveyid"]
#         }
