from django.views.generic import DetailView, ListView
from .models import Artigo
# Create your views here.

class ArtigoLista(ListView):
    model = Artigo

class ArtigoDetalhe(DetailView):
    model = Artigo


