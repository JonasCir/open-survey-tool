from django.urls import path

from results.views import SurveyResult, InternalResults

urlpatterns = [
    path('view/<uuid:survey_id>', SurveyResult.as_view(), name='result_view'),
    path('internaldemo', InternalResults.as_view(), name='internal_demo_view')
]
