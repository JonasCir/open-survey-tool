import pandas as pd

from responses.models import SurveyResponses
from surveys.models import Surveys


def mean_of_questions_in_category(df, dfa):
    df["Verhalten"] = dfa[["question2_1", "question2_2"]].mean(axis=1)
    df["Kompetenz"] = dfa[["question3_1", "question3_2"]].mean(axis=1)
    df["Information"] = dfa[["question4_1", "question4_2"]].mean(axis=1)
    df["Vertrauen"] = dfa[["question5_1", "question5_2"]].mean(axis=1)


def compute_mean():
    responses = pd.DataFrame.from_records(
        map(lambda x: x['response'], SurveyResponses.objects.all().values()))
    dfa = responses.replace(
        {"item1": 1.0, "item2": 2.0, "item3": 3.0, "item4": 4.0, "item5": None})
    mean_of_questions_in_category(dfa, dfa)
    return dfa, responses


def compute_role_per_context():
    dfa, responses = compute_mean()
    responses = responses.rename(
        columns={"question1_1": "Rolle", "question1_2": "Kontext"})
    dfz = responses[["Rolle", "Kontext"]]
    dft = dfz.value_counts().rename('Anzahl').to_frame()
    return dfa, responses, dft


def do_multi_index(dfa, dfax, dft):
    newindex = pd.MultiIndex.from_product([
        Surveys.get_survey_items_of_question('question1_1').keys(),
        Surveys.get_survey_items_of_question('question1_2').keys()],
        names=["Rolle", "Kontext"]
    )
    dftz = dft.reindex(newindex, fill_value=0)
    dfta = dftz.reset_index()
    dftax = dfta.set_index(["Rolle", "Kontext"])
    dfa["Rolle"] = dfax["Rolle"]
    dfa["Kontext"] = dfax["Kontext"]
    # print(dfa, dftax, "index", dfa.index, dftax.index)
    dfau = dfa.merge(dftax, left_on=["Rolle", "Kontext"], right_index=True)
    # print(dfau)
    dfau = dfau.replace({'Rolle': Surveys.get_survey_items_of_question('question1_1'),
                         'Kontext': Surveys.get_survey_items_of_question('question1_2')})
    dfau["Rolle-Kontext"] = dfau["Rolle"] + " bei " + dfau["Kontext"]
    return dfau


def compute_role_context():
    # get all ratings from the DB
    dfa, dfax, dft = compute_role_per_context()
    # print(dft)
    dfau = do_multi_index(dfa, dfax, dft)
    dfo = dfau[["Rolle-Kontext", "Verhalten",
                "Kompetenz", "Information", "Vertrauen"]]
    dfo = dfo.value_counts().rename('Anzahl').to_frame()
    df = dfo.reset_index()
    # print(df)
    return df
