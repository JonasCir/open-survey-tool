from rest_framework.serializers import ModelSerializer

from responses.models import SurveyResponses


class SurveyResponseSerializer(ModelSerializer):
    class Meta:
        model = SurveyResponses
        fields = ['id', 'survey', 'response']
