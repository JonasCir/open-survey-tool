import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from results.models import SurveyResult
from results.utils.figure import Figure

logger = get_logger()


class GeneralBubble(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = GeneralBubble.compute(mode)

        dft = df.value_counts().rename('Counting').to_frame()

        newindex = pd.MultiIndex.from_product([["item1", "item2", "item3", "item4"], [
            "item1", "item2", "item3", "item4", "item5"]], names=["question1-1", "question1-2"])

        dftaz = dft.reindex(newindex, fill_value=0)

        dfta = dftaz.reset_index()
        dfta = dfta.replace({'question1-1': {"item1": "Anzeigenerstatter:in",
                                             "item2": "Beschuldigte(r)", "item3": "Zeug(e):in",
                                             "item4": "Geschädigte(r)"},
                             'question1-2': {"item1": "Straßenverkehr allgemein", "item2": "Internetkriminalität",
                                             "item3": "Körperverletzungsdelikt",
                                             "item4": "Eigentumsdelikt",
                                             "item5": "Delikt gegen die sexuelle Selbstbestimmung"}})
        dfta = dfta.rename(columns={
            "question1-1": "Rolle", "question1-2": "Kontext", "Counting": "Teilnehmer"})

        fig = px.scatter(dfta, x="Rolle",
                         y="Kontext", size="Teilnehmer")
        fig.update_layout(
            title='Teilnehmer - Allgemeine Angaben',
            xaxis=dict(
                title='Rolle des Teilnehmers',
                gridcolor='white',
                gridwidth=2,
            ),
            yaxis=dict(
                title='Kontext des Teilnehmers',
                gridcolor='white',
                gridwidth=2
            ),
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)',
        )
        return fig.to_html(**cfg)

    @staticmethod
    def compute(mode):
        # get all ratings from the DB
        dfa = pd.DataFrame.from_records(
            map(lambda x: x['result'], SurveyResult.objects.all().values()))

        df = dfa[["question1-1", "question1-2"]]
        return df
