from django.urls import path
from results.views import InternalResults, SurveyResult

urlpatterns = [
    path("view/<uuid:survey_id>/", SurveyResult.as_view(), name="result_view"),
    path("internal/", InternalResults.as_view(), name="internal_results"),
]
