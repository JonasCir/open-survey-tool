import pandas as pd
import plotly.express as px

from open_survey_tool.utils.logger import get_logger
from responses.models import SurveyResponses
from results.utils.figure import Figure
from surveys.models import Surveys

logger = get_logger()


class GeneralBubble(Figure):

    @staticmethod
    def get_html(cfg, x_axis_question, y_axis_question):
        df = GeneralBubble.compute(x_axis_question, y_axis_question)

        dft = df.value_counts().rename('Counting').to_frame()

        newindex = pd.MultiIndex.from_product(
            [
                Surveys.get_survey_items_of_question(y_axis_question).keys(),
                Surveys.get_survey_items_of_question(x_axis_question).keys()
            ],
            names=[y_axis_question, x_axis_question]
        )

        dftaz = dft.reindex(newindex, fill_value=0)

        dfta = dftaz.reset_index()
        dfta = dfta.replace(
            {
                y_axis_question: Surveys.get_survey_items_of_question(y_axis_question),
                x_axis_question: Surveys.get_survey_items_of_question(
                    x_axis_question)
            }
        )

        dfta = dfta.rename(columns={
                           y_axis_question: 'Rolle', x_axis_question: 'Kontext', 'Counting': 'Teilnehmer'})

        fig = px.scatter(dfta, x='Rolle', y='Kontext', size='Teilnehmer')
        fig.update_layout(
            title='Teilnehmer - Allgemeine Angaben',
            xaxis={'title': 'Rolle des Teilnehmers',
                   'gridcolor': 'white', 'gridwidth': 2},
            yaxis={'title': 'Kontext des Teilnehmers',
                   'gridcolor': 'white', 'gridwidth': 2},
            paper_bgcolor='rgb(243, 243, 243)',
            plot_bgcolor='rgb(243, 243, 243)',
        )
        return fig.to_html(**cfg)

    @staticmethod
    def compute(x_axis_question, y_axis_question):
        # get all ratings from the DB
        dfa = pd.DataFrame.from_records(
            map(lambda x: x['response'],
                SurveyResponses.objects.all().values())
        )

        df = dfa[[y_axis_question, x_axis_question]]
        return df
