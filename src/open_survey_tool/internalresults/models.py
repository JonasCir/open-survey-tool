from django.db import models


class SurveyResult(models.Model):
    # survey = models.ForeignKey('survey.Surveys', on_delete=models.CASCADE)
    result = models.JSONField()
