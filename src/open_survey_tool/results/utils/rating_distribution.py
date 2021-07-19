import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from responses.models import SurveyResponses
from results.utils.figure import Figure
from surveys.models import Surveys

logger = get_logger()


class RatingDistribution(Figure):

    @staticmethod
    def get_html(cfg, question=None):
        try:
            res = RatingDistribution.compute(question)
        except Exception as e:
            logger.error(e)
            return ""
        fig = px.bar(res, labels={'value': 'Anzahl', 'variable': 'Variable'})

        fig.update_xaxes(type='category')
        fig.update_yaxes(tickformat=',d', automargin=False)

        return fig.to_html(**cfg)

    @staticmethod
    def compute(question):
        # get all ratings from the DB for the given question
        records = SurveyResponses.objects.values_list(f'response__{question}')
        df = pd.DataFrame.from_records(records)

        # map the items to human readable description
        question_items = Surveys.get_survey_items_of_question(question)
        df.replace(question_items, inplace=True)

        if df.empty:
            # todo maybe better redirect to custom page showing that now results are in now
            # we have a completely empty DB: return 0 counts for every question item
            zeros = [0 for _ in question_items.values()]
            df = pd.DataFrame({'Anzahl der Antworten': zeros}, index=question_items.values())
            df.rename_axis('Antwort', inplace=True)
            return df

        # group ratings by counts
        # count the values
        counts = df.value_counts().to_frame('Anzahl der Antworten')

        counts = counts.reset_index().set_index(0)

        # fill missing ratings
        res = counts.reindex(question_items.values(), fill_value=0)
        res.rename_axis('Antwort', inplace=True)
        return res
