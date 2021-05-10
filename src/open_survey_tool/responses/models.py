import uuid as uuid
from django.db import models


class SurveyResponses(models.Model):
    """
    Store the responses of a survey.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    survey = models.ForeignKey('surveys.Surveys', on_delete=models.CASCADE)
    response = models.JSONField()

