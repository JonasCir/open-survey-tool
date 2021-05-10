import logging

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from responses.models import SurveyResponses
from responses.serializers import SurveyResponseSerializer

logger = logging.getLogger(__name__)


class ResponseList(ListCreateAPIView):
    queryset = SurveyResponses.objects.all()
    serializer_class = SurveyResponseSerializer
    lookup_url_kwarg = 'survey_id'


class ResponseDetails(RetrieveUpdateDestroyAPIView):
    queryset = SurveyResponses.objects.all()
    serializer_class = SurveyResponseSerializer
    lookup_url_kwarg = 'survey_id'
