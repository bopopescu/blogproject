from django.shortcuts import render, redirect
from blogapp.models import Article
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q



def home(request):
    return render(request, 'home.html')


def list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'articles': articles})


def detail(request, title):
    article = Article.objects.filter(title=title)
    if article:
        article = article[0]
        return render(request, 'detail.html', {'article': article})


class create(CreateView):
    model = Article
    template_name = 'create.html'
    fields =['title','description','user']
    success_url = reverse_lazy('list')


def search(request):
    query = request.GET.get('query')
    if query:
        articles = Article.objects.filter(Q(title=query))
        return render(request, 'search.html', {'query': query, 'articles': articles})
        return render(request, 'search.html')


