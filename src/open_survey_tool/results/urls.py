from django.urls import path

from .views import Results, InternalResults

urlpatterns = [
    path('', Results.as_view(), name='public_results'),
    path('internal', InternalResults.as_view(), name='internal_results'),
]
