from django.urls import path
from .views import CreateSearchQueryView, ListSearchQueryView, GetSearchQueryView, GetListingsView

urlpatterns = [
    path('create-search-query', CreateSearchQueryView.as_view()),
    path('list-search-query', ListSearchQueryView.as_view()),
    path('get-search-query', GetSearchQueryView.as_view()),
    path('get-listings', GetListingsView.as_view()),
]
