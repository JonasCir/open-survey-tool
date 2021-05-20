import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from results.figures.utils import do_multi_index, compute_mean
from results.utils.figure import Figure

logger = get_logger()


class HeatMap(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = HeatMap.compute()

        fig = px.density_heatmap(df, y="Rolle-Kontext", x="Gesamtbewertung", nbinsy=20,
                                 color_continuous_scale="Viridis")
        fig.update_layout(
            title="Verteilung Teilnehmer",
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)'
        )

        return fig.to_html(**cfg)

    @staticmethod
    def compute():
        # get all ratings from the DB
        dfa, responses = compute_mean()
        dfa["Gesamtbewertung"] = dfa[["question2_1", "question2_2", "question3_1", "question3_2",
                                      "question4_1", "question4_2", "question5_1", "question5_2"]].mean(axis=1)

        responses = responses.rename(
            columns={"question1_1": "Rolle", "question1_2": "Kontext"})
        dfz = responses[["Rolle", "Kontext"]]
        dft = dfz.value_counts().rename('Anzahl').to_frame()
        # print(dft)

        dfau = do_multi_index(dfa, responses, dft)
        dfo = dfau[["Rolle-Kontext", "Verhalten", "Kompetenz",
                    "Information", "Vertrauen", "Gesamtbewertung"]]
        dfo = dfo.value_counts().rename('Anzahl').to_frame()
        df = dfo.reset_index()
        # print(df)
        return df
