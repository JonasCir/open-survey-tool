from django.urls import path

from .views import SurveyList, SurveyDetails, Survey, SurveyOverviewDetails, SurveyOverviewAll

urlpatterns = [
    path('', SurveyList.as_view(), name='surveys'),
    path('<uuid:survey_id>/', SurveyDetails.as_view(), name='survey_details'),
    path('view/<uuid:survey_id>/', Survey.as_view(), name='survey_view'),
    path('overview/', SurveyOverviewAll.as_view(), name='survey_overview_all'),
    path('overview/<uuid:survey_id>/', SurveyOverviewDetails.as_view(), name='survey_overview_details')
]
