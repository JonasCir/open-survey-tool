from django.urls import path

from .views import SurveyList, SurveyDetail, Survey, SurveyOverviewSingle, SurveyOverviewAll

urlpatterns = [
    path('', SurveyList.as_view(), name='surveys'),
    path('<int:pk>', SurveyDetail.as_view(), name='survey_details'),
    path('view/<int:surveyid>', Survey.as_view(), name='survey_view'),
    path('overview', SurveyOverviewAll.as_view(),
         name='survey_overview_all'),
    path('overview/<int:surveyid>', SurveyOverviewSingle.as_view(),
         name='survey_overview_single')
]
