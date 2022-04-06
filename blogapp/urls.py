from unicodedata import name
from django.urls import path
from . import views

# Define nome do app usado depois
app_name = "blogapp"
# Caminhos url do app
urlpatterns = [
    path("",views.ArtigoLista.as_view(),name="lista"),
    path("<slug:slug>/",views.ArtigoDetalhe.as_view(),name="detalhe")
]