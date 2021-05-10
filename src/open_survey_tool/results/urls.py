from django.urls import path

from results.views import SurveyResult

urlpatterns = [
    path('view/<uuid:survey_id>', SurveyResult.as_view(), name='result_view')
]
