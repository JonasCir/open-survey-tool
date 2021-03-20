import pandas as pd
import plotly.express as px

from results.figures.base import Figure
from results.models import SurveyResult


class RatingDistribution(Figure):

    @staticmethod
    def get_html(cfg):
        # get all ratings from the DB
        df = pd.DataFrame.from_records(map(lambda x: x['result'], SurveyResult.objects.all().values()))

        # group ratings by counts
        if df.empty is False:
            res = df['satisfaction'].value_counts().rename('count').to_frame()
        else:
            res = pd.DataFrame(data={'count': [0, 0, 0, 0, 0]})

        # rename the index column
        res.index.rename('rating', inplace=True)

        # fill missing ratings
        res = res.reindex(list(range(1, 6)), fill_value=0)

        fig = px.bar(res, labels={'value': 'count'})

        fig.update_xaxes(type='category')
        fig.update_yaxes(tickformat=',d', automargin=False)

        return fig.to_html(**cfg)
