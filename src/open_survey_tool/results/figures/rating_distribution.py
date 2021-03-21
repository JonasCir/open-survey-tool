import pandas as pd
import plotly.express as px

from results.figures.base import Figure
from results.models import SurveyResult


class RatingDistribution(Figure):

    @staticmethod
    def get_html(cfg, mode=None):
        res = RatingDistribution.compute(mode)
        fig = px.bar(res, labels={'value': 'Anzahl'})

        fig.update_xaxes(type='category')
        fig.update_yaxes(tickformat=',d', automargin=False)

        return fig.to_html(**cfg)

    @staticmethod
    def compute(mode=None):
        # get all ratings from the DB
        df = pd.DataFrame.from_records(
            map(lambda x: x['result'], SurveyResult.objects.all().values()))

        # group ratings by counts
        if df.empty is False:
            res = df[mode or 'satisfaction'].value_counts().rename('Personen').to_frame()
            res.index.rename('Bewertung', inplace=True)
        else:
            # we have a completely empty DB
            zeros = [0, 0, 0, 0] if mode == "question1-1" else [0, 0, 0, 0, 0]
            res = pd.DataFrame(data={'Bewertung': zeros})

        # fill missing ratings
        if mode == "question1-1":
            res = res.reindex(["item1", "item2", "item3",
                               "item4"], fill_value=0)
        else:
            res = res.reindex(["item1", "item2", "item3",
                               "item4", "item5"], fill_value=0)

        if mode == "question1-1":
            res = res.rename({"item1": "Anzeigenerstatter:in", "item2": "Beschuldigte(r)", "item3": "Zeug(e):in",
                              "item4": "Geschädigte(r)"}, axis='index')

        elif mode == "question1-2":
            res = res.rename({"item1": "Straßenverkehr allgemein", "item2": "Internetkriminalität",
                              "item3": "Körperverletzungsdelikt",
                              "item4": "Eigentumsdelikt", "item5": "Delikt gegen die sexuelle Selbstbestimmung"},
                             axis='index')
        else:
            res = res.rename({"item1": "Trifft voll zu", "item2": "Trifft zu", "item3": "Trifft weniger zu",
                              "item4": "Trifft gar nicht zu", "item5": "Keine Angabe"}, axis='index')

        return res
