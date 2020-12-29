from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
# Create your views here.
def homepage(request):
    homepage = request.GET.get('homepage')
    return render(request,'homepage.html',{})

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page') # 3 posts in each page page = request.GET.get('page')
    try:
        posts = paginator.page(page) 
    except PageNotAnInteger:
               # If page is not an integer deliver the first page
        posts = paginator.page(1) 
    except EmptyPage:
               # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'list.html',{'posts':posts,'page':page})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post,slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
	return render(request, 'detail.html',
                     {'post': post})

def card_view(request):
    image = request.GET.get('image')
    return render(request,'image.html',{image:'image'})

def christmas_cards(request):
    image = request.GET.get('image')
    return render(request,'christmas_cards.html',{image:'image'})

def hanukkah_cards(request):
    image = request.GET.get('image')
    return render(request,'hanukkah_cards.html',{image:'image'})

def kwanzaa_cards(request):
    image = request.GET.get('image')
    return render(request,'kwanzaa_cards.html',{image:'image'})

def boxing_day_cards(request):
    image = request.GET.get('image')
    return render(request,'boxing_day_cards.html',{image:'image'})

def omisoka_cards(request):
    image = request.GET.get('image')
    return render(request,'omisoka_cards.html',{image:'image'})


def saint_nickolas_day_cards(request):
    image = request.GET.get('image')
    return render(request,'saint_nickolas_day_cards.html',{image:'image'})

def winter_solstice_cards(request):
    image = request.GET.get('image')
    return render(request,'winter_solstice_cards.html',{image:'image'})

def mardi_gras_cards(request):
    image = request.GET.get('image')
    return render(request,'mardi_gras_cards.html',{image:'image'})


def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})


def post_search(request): 
    form = SearchForm() 
    Search = None
    results = []
    if 'Search' in request.GET:
        form = SearchForm(request.GET) 
        if form.is_valid():
            Search = form.cleaned_data['Search'] 
            results = Post.published.annotate(search=SearchVector('title', 'body'), ).filter(search=Search)
    return render(request,'search.html', {'form': form,'Search': Search, 'results': results})






