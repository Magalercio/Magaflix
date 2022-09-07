from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def homepage(request):
#    return render(request, "homepage.html")
# Usando Class Base Views ao invés de Function base view


class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:# usuario não está autenticado
            return redirect('filme:homefilmes')
            #redirecionar para homefilmes.
        else:
            return super().get(request, *args, **kwargs) # redireciona para homepage

# def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes']= lista_filmes
#   return render(request, "homefilmes.html", context)


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme  # vai pro html como object_list


class Detalhesfilme (LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do modelo

    def get(self, request, *args, **kwargs):
        # descobrir qual filme ele ta acessando
        filme = self.get_object()
        # somar 1 nas visualizaçoes daquele filme
        filme.visualizacoes += 1
        #salvar
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) #redireciona o usuário para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # self.get_object()
        filmes_relacionados =self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    #editando o object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class Criarconta(TemplateView):
    template_name = "criarconta.html"