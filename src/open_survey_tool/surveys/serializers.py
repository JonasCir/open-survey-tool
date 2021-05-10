from rest_framework.serializers import ModelSerializer

from surveys.models import Surveys


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Surveys
        fields = ['uuid', 'name', 'definition_json']
