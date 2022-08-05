from django.urls import path

from .views import (
    AnagraficaCreateView,
    AnagraficaListView,
    AnagraficaDetailView,
    AnagraficaUpdateView,
    AnagraficaDeleteView,
    AnagraficaMenuView,
    search_anagrafica
)

app_name = 'anagrafica'
 
urlpatterns = [
    path('', AnagraficaMenuView.as_view(), name='anagrafica-menu'),
    path('list/', AnagraficaListView.as_view(), name='anagrafica-list'),
    path('create/', AnagraficaCreateView.as_view(), name='anagrafica-create'),
    path('<int:id>/', AnagraficaDetailView.as_view(), name='anagrafica-detail'),
    path('<int:id>/update/', AnagraficaUpdateView.as_view(), name='anagrafica-update'),
    path('<int:id>/delete/', AnagraficaDeleteView.as_view(), name='anagrafica-delete'),
    path('search', search_anagrafica, name='search-anagrafica')
]  