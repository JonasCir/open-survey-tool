import pandas as pd
import plotly.express as px

from results.figures.base import Figure
from results.models import SurveyResult


class RatingDistribution(Figure):

    @staticmethod
    def get_html():
        df = pd.DataFrame.from_records(map(lambda x: x['result'], SurveyResult.objects.all().values()))

        fig = px.bar(df)
        return fig.to_html(**Figure.html_config)
