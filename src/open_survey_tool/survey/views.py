from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from open_survey_tool.utils.logger import get_logger

logger = get_logger()


class Survey(TemplateView):
    template_name = "survey/survey.html"

    def get_context_data(self, **kwargs):
        return {}


class SurveyContent(View):
    def get(self, request):
        logger.info('sending out survey')

        content = {
            'questions': [
                {
                    "type": "html",
                    "name": "section1",
                    "html": "<h2>1. Allgemeine Informationen</h2>"
                },
                {
                    "type": "radiogroup",
                    "name": "question1-1",
                    "indent": 2,
                    "title": "1.1: In welcher Rolle sind Sie der Polizei begegnet?",
                    "hideNumber": "true",
                    "isRequired": "true",
                    "choices": [
                        {
                            "value": "item1",
                            "text": "Anzeigenerstatter:in"
                        },
                        {
                            "value": "item2",
                            "text": "Beschuldigte(r)"
                        },
                        {
                            "value": "item3",
                            "text": "Zeug(e):in"
                        },
                        {
                            "value": "item4",
                            "text": "Geschädigte(r)"
                        }
                    ],
                    "colCount": 2
                },
                {
                    "type": "radiogroup",
                    "name": "question1-2",
                    "indent": 2,
                    "title": "1.2: In welchem Kontext hatten Sie mit der Polizei zu tun?",
                    "hideNumber": "true",
                    "isRequired": "true",
                    "choices": [
                        {
                            "value": "item1",
                            "text": "Straßenverkehr allgemein"
                        },
                        {
                            "value": "item2",
                            "text": "Internetkriminalität"
                        },
                        {
                            "value": "item3",
                            "text": "Körperverletzungsdelikt"
                        },
                        {
                            "value": "item4",
                            "text": "Eigentumsdelikt"
                        },
                        {
                            "value": "item5",
                            "text": "Delikt gegen die sexuelle Selbstbestimmung"
                        }
                    ],
                    "colCount": 3
                },
                {
                    "type": "html",
                    "name": "section2",
                    "html": "<h2>2. Verhalten und Auftreten</h2>"
                },
                {
                    "type": "rating",
                    "name": "question2-1",
                    "indent": 2,
                    "title": "2.1: Das Auftreten der Polizeibeamten war professionell!",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "rating",
                    "name": "question2-2",
                    "indent": 2,
                    "title": "2.2: Die Kommunikation der Polizeibeamten war zu jederzeit angemessen!",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "html",
                    "name": "section3",
                    "html": "<h2>3. Kompetenz</h2>"
                },
                {
                    "type": "rating",
                    "name": "question3-1",
                    "indent": 2,
                    "title": "3.1: Die Polizeibeamten waren zu Ihrem Anliegen jederzeit auskunftsfähig!",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "rating",
                    "name": "question3-2",
                    "indent": 2,
                    "title": "3.2: Die Polizeibeamten konnten Ihr Anliegen rechtlich einordnen!",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "html",
                    "name": "section4",
                    "html": "<h2>4. Information</h2>"
                },
                {
                    "type": "rating",
                    "name": "question4-1",
                    "indent": 2,
                    "title": "4.1: Wurden Sie in der Situation ausreichend informiert?",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "rating",
                    "name": "question4-2",
                    "indent": 2,
                    "title": "4.2: Wurden Sie über die weiteren Maßnahmen ausreichend informiert?",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "html",
                    "name": "section5",
                    "html": "<h2>5. Vertrauen</h2>"
                },
                {
                    "type": "rating",
                    "name": "question5-1",
                    "indent": 2,
                    "title": "5.1: Hatten Sie in Ihrem Anliegen Vertrauen in die Aufgabenwahrnehmung der Polizei?",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                },
                {
                    "type": "rating",
                    "name": "question5-2",
                    "indent": 2,
                    "title": "5.2: Würden Sie sich auch künftig vertrauensvoll an die Polizei wenden?",
                    "hideNumber": "true",
                    "rateValues": [
                        {
                            "value": "item1",
                            "text": "Trifft voll zu"
                        },
                        {
                            "value": "item2",
                            "text": "Trifft zu"
                        },
                        {
                            "value": "item3",
                            "text": "Trifft weniger zu"
                        },
                        {
                            "value": "item4",
                            "text": "Trifft gar nicht zu"
                        },
                        {
                            "value": "item5",
                            "text": "Keine Angabe"
                        }
                    ]
                }
            ]
        }
        return JsonResponse(content)
