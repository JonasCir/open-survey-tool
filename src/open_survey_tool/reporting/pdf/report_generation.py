import io

import pdfkit
from django.core.files.temp import NamedTemporaryFile
from django.template import loader

from responses.utils.figure import Figure
from responses.views import SurveyResponse

template = loader.get_template('reporting/pdf/report.html')
cfg = Figure.pdf_config


def generate_pdf_report():
    """
    Render an HTML template and fill in the context. Convert it to PDF and return the report.
    :return: An in-memory byte buffer which holds the generated PDF.
    :rtype io.BytesIO
    """

    context = {
        'introduction': 'Quidem natus voluptatibus laboriosam quis aspernatur voluptatem optio provident.',
        'results': SurveyResponse.create_context_data()['results']
    }

    rendered = template.render(context)

    # FIXME(@JonasCir) use BytesIO directly instead of filesystem
    #  see https://github.com/JazzCore/python-pdfkit/issues/178

    with NamedTemporaryFile() as tmp_file:
        name = tmp_file.name
        # todo cover page supported
        pdfkit.from_string(rendered, name)
        with open(name, 'rb') as f:
            pdf = io.BytesIO(f.read())
            return pdf
