from django.urls import path

from .views import Results

urlpatterns = [
    path('', Results.as_view(), name='results'),
]
