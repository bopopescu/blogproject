from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from blogapp.models import Article,CustomUser
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from blogapp.forms import ArticleForm,CustomUserCreationForm

@login_required
def home(request):
    user_articles_count = Article.objects.filter(user=request.user).count()
    user_articles = Article.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'articles':user_articles,'count':user_articles_count})


def list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'articles': articles})


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    print(article)
    return render(request, 'detail.html', {'article': article})


def create(request):
    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            created_at=form.cleaned_data['created_at']
            user=request.user
            article=Article(title=title,created_at=created_at,user=user)
            article.save()
            return redirect('list')
        else:
            form=ArticleForm()
    return render(request,'create.html',{'form':form})


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
            #email=form.cleaned_data['email']
            #image=form.cleaned_data['image']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class Update(UpdateView,):
    model = Article
    template_name = 'update.html'
    fields = ['title','description']
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    model=Article
    template_name = 'delete.html'
    success_url = reverse_lazy('home')