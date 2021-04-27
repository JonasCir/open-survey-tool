import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from results.models import SurveyResponses
from results.utils.figure import Figure
from survey.models import Surveys

logger = get_logger()


class RatingDistribution(Figure):

    @staticmethod
    def get_html(cfg, question=None):
        res = RatingDistribution.compute(question)
        fig = px.bar(res, labels={'value': 'Anzahl'})

        fig.update_xaxes(type='category')
        fig.update_yaxes(tickformat=',d', automargin=False)

        return fig.to_html(**cfg)

    @staticmethod
    def compute(question):
        # get all ratings from the DB for the given question
        df = pd.DataFrame.from_records(
            SurveyResponses.objects.values_list(f'response__{question}')
        )

        # map the items to human readable description
        question_items = Surveys.get_survey_items_for_question(question)
        df.replace(question_items, inplace=True)

        # group ratings by counts
        if df.empty is False:
            # count the values
            dist = df.value_counts().to_frame('distribution')
        else:
            # we have a completely empty DB
            zeros = [0 for _ in question_items.values()]
            dist = pd.DataFrame(data={'distribution': zeros})

        dist = dist.reset_index().set_index(0)

        # fill missing ratings
        res = dist.reindex(question_items.values(), fill_value=0)

        return res
