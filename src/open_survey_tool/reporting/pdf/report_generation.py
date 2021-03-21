import io

import pdfkit
from django.core.files.temp import NamedTemporaryFile
from django.template import loader

from results.figures.base import Figure
from results.figures.gapminder import Gapminder
from results.figures.rating_distribution import RatingDistribution

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
        'rating_1_1': RatingDistribution.get_html(cfg, "question1-1"),
        'rating_1_2': RatingDistribution.get_html(cfg, "question1-2"),
        'rating_2_1': RatingDistribution.get_html(cfg, "question2-1"),
        'rating_2_2': RatingDistribution.get_html(cfg, "question2-2"),
        'rating_3_1': RatingDistribution.get_html(cfg, "question3-1"),
        'rating_3_2': RatingDistribution.get_html(cfg, "question3-2"),
        'rating_4_1': RatingDistribution.get_html(cfg, "question4-1"),
        'rating_4_2': RatingDistribution.get_html(cfg, "question4-2"),
        'rating_5_1': RatingDistribution.get_html(cfg, "question5-1"),
        'rating_5_2': RatingDistribution.get_html(cfg, "question5-2"),
        'gapminder': Gapminder.get_html(cfg)
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
