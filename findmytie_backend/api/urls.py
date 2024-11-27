from django.urls import path
from .views import CreateSearchQueryView, SearchQueryView 

urlpatterns = [
    path('create-search-query', CreateSearchQueryView.as_view()),
    path('view-search-query', SearchQueryView.as_view()),
]
