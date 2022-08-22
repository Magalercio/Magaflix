from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
# def homepage(request):
#    return render(request, "homepage.html")
# Usando Class Base Views ao invés de Function base view


class Homepage(TemplateView):
    template_name = "homepage.html"

# def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes']= lista_filmes
#   return render(request, "homefilmes.html", context)

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme  # vai pro html como object_list


class Detalhesfilme (DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do modelo