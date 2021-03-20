import plotly.express as px

from results.figures.base import Figure


class Gapminder(Figure):

    @staticmethod
    def get_html(cfg):
        df = px.data.gapminder().query("continent=='Oceania'")
        fig = px.line(df, x="year", y="lifeExp", color='country')
        return fig.to_html(**cfg)
