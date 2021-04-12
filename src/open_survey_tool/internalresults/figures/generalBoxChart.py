import pandas as pd
import plotly.express as px

from internalresults.figures.base import Figure
from results.models import SurveyResult

from open_survey_tool.utils.logger import get_logger

logger = get_logger()


class GeneralBoxChart(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        df = GeneralBoxChart.compute(mode)

        if mode == "Verhalten":
            titletext = "Ergebnis Verhalten (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle", "Auftreten", "Kommunikation"]]
        elif mode == "Kompetenz":
            titletext = "Ergebnis Kompetenz (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle",  "Auskunftsfähig", "Einordnen"]]
        elif mode == "Information":
            titletext = "Ergebnis Information (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle",  "Information Situation",
                      "Information weitere Maßnahmen"]]
        elif mode == "Vertrauen":
            titletext = "Ergebnis Vertrauen (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle",
                      "Aufgabenwahrnehmung", "Vertrauen allgemein"]]
        else:
            titletext = "Ergebnis Übersicht (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle", "Verhalten",
                      "Kompetenz", "Information", "Vertrauen"]]

        fig = px.box(dfp, points="all", color="Rolle")

        fig.update_layout(
            title=titletext,
            xaxis=dict(
                title='Fragen',
                gridcolor='white',
                gridwidth=2,
            ),
            yaxis=dict(
                title='Bewertung',
                gridcolor='white',
                gridwidth=2
            ),
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)',
        )

        return fig.to_html(**cfg)

    @ staticmethod
    def compute(mode):
        # get all ratings from the DB
        dfax = pd.DataFrame.from_records(
            map(lambda x: x['result'], SurveyResult.objects.all().values()))

        dfa = dfax.replace(
            {"item1": 1.0, "item2": 2.0, "item3": 3.0, "item4": 4.0, "item5": None})

        df = dfa
        df = df.rename(columns={
            "question2-1": "Auftreten", "question2-2": "Kommunikation"})

        df = df.rename(columns={
            "question3-1": "Auskunftsfähig", "question3-2": "Einordnen"})

        df = df.rename(columns={
            "question4-1": "Information Situation", "question4-2": "Information weitere Maßnahmen"})

        df = df.rename(columns={
            "question5-1": "Aufgabenwahrnehmung", "question5-2": "Vertrauen allgemein"})

        df["Verhalten"] = dfa[["question2-1", "question2-2"]].mean(axis=1)
        df["Kompetenz"] = dfa[["question3-1", "question3-2"]].mean(axis=1)
        df["Information"] = dfa[[
            "question4-1", "question4-2"]].mean(axis=1)
        df["Vertrauen"] = dfa[[
            "question5-1", "question5-2"]].mean(axis=1)
        df["Rolle"] = dfax["question1-1"]
        df["Kontext"] = dfax["question1-2"]
        df = df.replace({'Rolle': {"item1": "Anzeigenerstatter:in",
                                   "item2": "Beschuldigte(r)", "item3": "Zeug(e):in", "item4": "Geschädigte(r)"},
                         'Kontext': {"item1": "Straßenverkehr allgemein", "item2": "Internetkriminalität",
                                     "item3": "Körperverletzungsdelikt",
                                     "item4": "Eigentumsdelikt", "item5": "Delikt gegen die sexuelle Selbstbestimmung"}})

        df["Rolle-Kontext"] = df["Rolle"] + " bei " + df["Kontext"]

        return df
