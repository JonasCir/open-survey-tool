from django.db import models


class SurveyResponses(models.Model):
    """
    Store the responses of a survey.
    """
    # survey = models.ForeignKey('survey.Surveys', on_delete=models.CASCADE)
    response = models.JSONField()


class SurveyResults(models.Model):
    """
    Stores the information how a certain question should be shown as result.
    """
    # survey = models.ForeignKey('survey.Surveys', on_delete=models.CASCADE)
    question = models.CharField(max_length=32)

    class Result(models.TextChoices):
        GENERAL_BUBBLE = 'gn_bbbl'
        GENERAL_BOX_CHART = 'gn_bx_chrt'
        SCATTER_MATRIX = 'scat_mtrx'
        PIE_CHART = 'pie_chrt'
        HEAT_MAP = 'ht_map'

    result = models.CharField(
        max_length=16,
        choices=Result.choices
    )
