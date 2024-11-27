from django.urls import path
from .views import CreateSearchQueryView, SearchQueryView 

urlpatterns = [
    path('create', CreateSearchQueryView.as_view()),
    path('view', SearchQueryView.as_view()),
]
