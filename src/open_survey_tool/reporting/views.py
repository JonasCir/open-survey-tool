from django.http import FileResponse
from django.views.generic import TemplateView

from reporting.pdf.report_generation import generate_pdf_report


class ReportingOverview(TemplateView):
    template_name = 'reporting/index.html'

    def get_context_data(self, **kwargs):
        return {}


def get_report(request):
    """
    Generate a report. Currently a simple PDF report ist templated and returned.
    :return: A generated PDF file report.
    """
    pdf_report = generate_pdf_report()
    return FileResponse(pdf_report, as_attachment=True, filename='sormas_stats_report.pdf')
