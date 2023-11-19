from django.urls import path
from logingest.views import *

urlpatterns = [
    path('search/', LogQueryView.as_view({'get': 'list'})),
     path("update/",LogIngestView.as_view())
]