from django.urls import path

from . import views
from .views import ReportingOverview

urlpatterns = [
    path('', ReportingOverview.as_view(), name='reporting'),
    path('get_report/', views.get_report, name='get_report'),
]
