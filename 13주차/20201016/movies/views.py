from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.core.paginator import Paginator
from .models import Movie


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    page = int(request.GET.get('page', 1) or 1)
    paginator = Paginator(movies, 3)
    movies = paginator.get_page(page)

    page_numbers_range = 5

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    context = {
        'movies': movies,
        'paginator_range': paginator_range,    
    }
    return render(request, 'movies/index.html',context)
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request):
    movies = Movie.objects.filter(vote_average__gte=8.7)
    page = int(request.GET.get('page', 1) or 1)
    paginator = Paginator(movies, 3)
    movies = paginator.get_page(page)

    page_numbers_range = 5

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    context = {
        'movies': movies,
        'paginator_range': paginator_range,    
    }
    return render(request, 'movies/recommended.html',context)