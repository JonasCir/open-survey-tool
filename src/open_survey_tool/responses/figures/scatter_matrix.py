import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from responses.figures.utils import compute_role_context
from responses.utils.figure import Figure

logger = get_logger()


class ScatterMatrix(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = ScatterMatrix.compute()
        fig = px.scatter_matrix(df, dimensions=["Verhalten", "Kompetenz", "Information", "Vertrauen"],
                                color="Rolle-Kontext", size="Anzahl")
        fig.update_traces(diagonal_visible=False)
        fig.update_layout(
            title="Zufriedenheit unter den Teilnehmern",
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)'
        )

        return fig.to_html(**cfg)

    @staticmethod
    def compute():
        return compute_role_context()
