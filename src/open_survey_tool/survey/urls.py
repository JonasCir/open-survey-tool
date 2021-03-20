from django.urls import path

from .views import Survey, SurveyContent

urlpatterns = [
    path('', Survey.as_view(), name='survey'),
    path('content', SurveyContent.as_view(), name='survey_content')
]
