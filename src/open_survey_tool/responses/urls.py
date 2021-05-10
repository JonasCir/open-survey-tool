from django.urls import path

from .views import ResponseList, ResponseDetails

urlpatterns = [
    path('', ResponseList.as_view(), name='responses'),
    path('<uuid:survey_id>', ResponseDetails.as_view(), name='response_details')
]
