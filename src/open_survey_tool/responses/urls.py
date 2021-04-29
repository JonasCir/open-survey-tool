from django.urls import path

from .views import InternalResults, ResponseList, ResponseDetail, SurveyResponse

urlpatterns = [
    path('', ResponseList.as_view(), name='responses'),
    path('<int:pk>', ResponseDetail.as_view(), name='response_details'),
    path('view/<int:pk>', SurveyResponse.as_view(), name='response_view'),
    path('internal/', InternalResults.as_view(), name='response_internal_view'),
]
