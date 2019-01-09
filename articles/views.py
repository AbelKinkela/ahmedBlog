from django.shortcuts import render, get_object_or_404
from .models import Article, ExtraContent
from django.core.paginator import Paginator
import random

# Create your views here.


def articles(request):
    articles = Article.objects.all().order_by('-published')

    paginator = Paginator(articles, 5)  # Show 5 articles per page

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'articles/articles.html', {'articles': articles})


def home(request):
    extras = ExtraContent.objects.get(id=1)
    mostRecents = Article.objects.all().order_by('-published')[:3]
    return render(request, 'articles/home.html', {'extras': extras, 'mostRecents': mostRecents})


def book_recomendation(request):
    return render(request, 'articles/book_recomendation.html')


def about(request):
    return render(request, 'articles/about.html')


def contact(request):
    return render(request, 'articles/contact.html')


def reading(request, title):
    # get all articles except the current
    temp = Article.objects.exclude(title=title)
    # cast the queryset as a list
    listTemp = list(temp)
    # shuffle the list
    random.shuffle(listTemp)
    # just pick the first element
    nextArticle = listTemp[0]
    article_detail = get_object_or_404(Article, title=title)
    return render(request, 'articles/reading.html', {'article': article_detail, 'nextArticle': nextArticle})
