from django.shortcuts import render, redirect,HttpResponse
from blogapp.models import Article
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user_articles_count = Article.objects.filter(user=request.user).count()
    user_articles = Article.objects.filter(user=request.user)
    return render(request, 'home.html', {'articles':user_articles,'count':user_articles_count})


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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})