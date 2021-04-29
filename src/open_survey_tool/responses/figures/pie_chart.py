import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from responses.figures.utils import compute_role_context
from responses.utils.figure import Figure

logger = get_logger()


class PieChart(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = PieChart.compute()

        fig = px.pie(df, names="Rolle-Kontext", values="Anzahl")
        fig.update_layout(
            title="Verteilung Teilnehmer",
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)'
        )

        return fig.to_html(**cfg)

    @staticmethod
    def compute():
        return compute_role_context()
