import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from results.models import SurveyResult
from results.utils.figure import Figure

logger = get_logger()


class PieChart(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = PieChart.compute(mode)

        fig = px.pie(df, names="Rolle-Kontext", values="Anzahl")
        fig.update_layout(
            title="Verteilung Teilnehmer",
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)'
        )

        return fig.to_html(**cfg)

    @staticmethod
    def compute(mode):
        # get all ratings from the DB
        dfax = pd.DataFrame.from_records(
            map(lambda x: x['result'], SurveyResult.objects.all().values()))

        dfa = dfax.replace(
            {"item1": 1.0, "item2": 2.0, "item3": 3.0, "item4": 4.0, "item5": None})
        dfa["Verhalten"] = dfa[["question2-1", "question2-2"]].mean(axis=1)
        dfa["Kompetenz"] = dfa[["question3-1", "question3-2"]].mean(axis=1)
        dfa["Information"] = dfa[[
            "question4-1", "question4-2"]].mean(axis=1)
        dfa["Vertrauen"] = dfa[[
            "question5-1", "question5-2"]].mean(axis=1)

        dfax = dfax.rename(columns={
            "question1-1": "Rolle", "question1-2": "Kontext"})
        dfz = dfax[["Rolle", "Kontext"]]
        dft = dfz.value_counts().rename('Anzahl').to_frame()
        # print(dft)

        newindex = pd.MultiIndex.from_product([["item1", "item2", "item3", "item4"], [
            "item1", "item2", "item3", "item4", "item5"]], names=["Rolle", "Kontext"])

        dftz = dft.reindex(newindex, fill_value=0)

        dfta = dftz.reset_index()

        dftax = dfta.set_index(["Rolle", "Kontext"])
        dfa["Rolle"] = dfax["Rolle"]
        dfa["Kontext"] = dfax["Kontext"]
        # print(dfa, dftax, "index", dfa.index, dftax.index)
        dfau = dfa.merge(dftax, left_on=[
            "Rolle", "Kontext"], right_index=True)
        # print(dfau)

        dfau = dfau.replace({'Rolle': {"item1": "Anzeigenerstatter:in",
                                       "item2": "Beschuldigte(r)", "item3": "Zeug(e):in", "item4": "Geschädigte(r)"},
                             'Kontext': {"item1": "Straßenverkehr allgemein", "item2": "Internetkriminalität",
                                         "item3": "Körperverletzungsdelikt",
                                         "item4": "Eigentumsdelikt",
                                         "item5": "Delikt gegen die sexuelle Selbstbestimmung"}})

        dfau["Rolle-Kontext"] = dfau["Rolle"] + " bei " + dfau["Kontext"]
        dfo = dfau[["Rolle-Kontext", "Verhalten",
                    "Kompetenz", "Information", "Vertrauen"]]
        dfo = dfo.value_counts().rename('Anzahl').to_frame()
        df = dfo.reset_index()
        # print(df)
        return df
