from django.db import models


class Surveys(models.Model):
    name = models.CharField(max_length=32)
