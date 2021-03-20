import io

import pdfkit
from django.core.files.temp import NamedTemporaryFile
from django.template import loader

from results.figures.base import Figure
from results.figures.gapminder import Gapminder
from results.figures.rating_distribution import RatingDistribution

template = loader.get_template('reporting/pdf/report.html')
cdf = Figure.pdf_config


def generate_pdf_report():
    """
    Render an HTML template and fill in the context. Convert it to PDF and return the report.
    :return: An in-memory byte buffer which holds the generated PDF.
    :rtype io.BytesIO
    """
    context = {
        'introduction': 'Quidem natus voluptatibus laboriosam quis aspernatur voluptatem optio provident.',
        'gapminder': Gapminder.get_html(cdf),
        'rating_dist': RatingDistribution.get_html(cdf)
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
