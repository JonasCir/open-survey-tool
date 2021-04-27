import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from results.figures.utils import mean_of_questions_in_category
from results.models import SurveyResponses
from results.utils.figure import Figure
from survey.models import Surveys

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
            dfp = df[["Rolle", "Auskunftsfähig", "Einordnen"]]
        elif mode == "Information":
            titletext = "Ergebnis Information (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle", "Information Situation", "Information weitere Maßnahmen"]]
        elif mode == "Vertrauen":
            titletext = "Ergebnis Vertrauen (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle", "Aufgabenwahrnehmung", "Vertrauen allgemein"]]
        else:
            titletext = "Ergebnis Übersicht (1=sehr zufrieden, 4=sehr unzufrieden)"
            dfp = df[["Rolle", "Verhalten", "Kompetenz", "Information", "Vertrauen"]]

        fig = px.box(dfp, points="all", color="Rolle")

        fig.update_layout(
            title=titletext,
            xaxis={'title': 'Fragen', 'gridcolor': 'white', 'gridwidth': 2},
            yaxis={'title': 'Bewertung', 'gridcolor': 'white', 'gridwidth': 2},
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)',
        )

        return fig.to_html(**cfg)

    @staticmethod
    def compute(mode):
        # get all ratings from the DB
        dfax = pd.DataFrame.from_records(
            map(lambda x: x['response'], SurveyResponses.objects.all().values())
        )

        dfa = dfax.replace({"item1": 1.0, "item2": 2.0, "item3": 3.0, "item4": 4.0, "item5": None})

        df = dfa
        df = df.rename(columns={"question2_1": "Auftreten", "question2_2": "Kommunikation"})

        df = df.rename(columns={"question3_1": "Auskunftsfähig", "question3_2": "Einordnen"})

        df = df.rename(columns={"question4_1": "Information Situation", "question4_2": "Information weitere Maßnahmen"})

        df = df.rename(columns={"question5_1": "Aufgabenwahrnehmung", "question5_2": "Vertrauen allgemein"})

        mean_of_questions_in_category(df, dfa)
        df["Rolle"] = dfax["question1_1"]
        df["Kontext"] = dfax["question1_2"]

        df = df.replace({
            'Rolle': Surveys.get_survey_items_for_question('question1_1'),
            'Kontext': Surveys.get_survey_items_for_question('question1_2')}
        )

        df["Rolle-Kontext"] = df["Rolle"] + " bei " + df["Kontext"]

        return df


