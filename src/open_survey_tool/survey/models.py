import json

from django.db import models, connection


class Surveys(models.Model):
    name = models.CharField(max_length=32)
    definition_json = models.JSONField(default=dict)

    @staticmethod
    def get_survey_type_by_question(question):
        """
        Returns the survey.js question type for a given question.
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT elem  -> 'type' AS type 
                FROM survey_surveys, jsonb_array_elements(definition_json -> 'questions') AS elem
                WHERE elem -> 'name' ? %s;
                """,
                [question]
            )
            t = cursor.fetchone()[0]
            # todo enforce uniqueness in DB
            tmp = json.loads(t)
            return tmp

    @staticmethod
    def get_survey_items_for_question(question):
        """
        Return the question items (the item name and the human readable name) as dict.
        :param question:
        :return:
        """
        _type = Surveys.get_survey_type_by_question(question)

        type_to_item_key = {'radiogroup': 'choices', 'rating': 'rateValues'}
        item_key = type_to_item_key[_type]
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT elem -> %s AS items FROM 
                survey_surveys, jsonb_array_elements(definition_json -> 'questions') 
                AS elem
                WHERE elem -> 'name' ? %s;
                """,
                [item_key, question]
            )
            t = cursor.fetchone()[0]
            # todo enforce uniqueness in DB
            tmp = json.loads(t)
            return {elem['value']: elem['text'] for elem in tmp}
