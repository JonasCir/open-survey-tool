from django.urls import path

from .views import SurveyList, SurveyDetail, Survey

urlpatterns = [
    path('', SurveyList.as_view(), name='surveys'),
    path('<int:pk>', SurveyDetail.as_view(), name='survey_details'),
    path('view/<int:pk>', Survey.as_view(), name='survey_view')
]
