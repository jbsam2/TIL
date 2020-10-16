from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .models import Review, Comment
from movies.models import Movie,Genre
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse
import math,random


def main(request):
    movies = Movie.objects.all()
    movie1 = random.choice(movies)
    movie2 = random.choice(movies)
    movie3 = random.choice(movies)
    context = {
        'movie1': movie1,
        'movie2': movie2,
        'movie3': movie3,
    }
    return render(request,'community/main.html', context)

def index(request):
    return render(request,'community/index.html')

def review_list(request):
    reviews = Review.objects.all()
    page = int(request.GET.get('page', 1) or 1)
    paginator = Paginator(reviews, 3)
    reviews = paginator.get_page(page)

    page_numbers_range = 5

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    context = {
        'reviews': reviews,
        'paginator_range': paginator_range,    
    }
    return render(request, 'community/review_list.html',context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)


def detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review':review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/review_detail.html',context)


@require_POST
def comments_create(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('community:detail', review.pk)
        context = {
            'comment_form': comment_form,
            'review': review,
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')


@require_POST
def like_list(request, review_pk):
    like_status ={
        'error':'unauthorized',
    }
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            liked=False
        else:
            review.like_users.add(request.user)
            liked=True
        like_status = {
            'liked':liked,
            'count':review.like_users.count(),
        }
    return JsonResponse(like_status)


@require_POST
def like_detail(request, review_pk):
    like_status ={
        'error':'unauthorized',
    }
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            liked = False
        else:
            review.like_users.add(request.user)
            liked = True
        like_status = {
            'liked':liked,
            'count':review.like_users.count(),
        }
    return JsonResponse(like_status)


def search(request):
    kind = request.GET.get('kind')
    keyword = request.GET.get('keyword')
    if kind == 'title':
        if Review.objects.filter(title__icontains=keyword).exists():
            ret = Review.objects.filter(title__icontains=keyword)
            context = {
                'reviews':ret,
            }
            return render(request, 'community/review_list.html',context)
    elif kind == 'person':
        if get_user_model().objects.filter(username__icontains=keyword).exists():
            person = get_user_model().objects.filter(username__icontains=keyword)
            context = {
                'persons':person,
            }
            return render(request, 'accounts/profile_list.html',context)
    elif kind =='content':
        if Review.objects.filter(content__icontains=keyword).exists():
            ret = Review.objects.filter(content__icontains=keyword)
            context = {
                'reviews':ret,
            }
            return render(request, 'community/review_list.html',context)
    elif kind =="movie_title_review":
        if Review.objects.filter(movie_title__icontains=keyword).exists():
            ret = Review.objects.filter(movie_title__icontains=keyword)
            context = {
                'reviews':ret,
            }
            return render(request, 'community/review_list.html',context)
    elif kind =="movie_title_movie":
        if Movie.objects.filter(title__icontains=keyword).exists():
            ret = Movie.objects.filter(title__icontains=keyword)
            context = {
                'movies':ret,
            }
            return render(request, 'movies/index.html',context)
    elif kind =="genres":
        change = {
            '모험':12,'판타지':14,'애니메이션':16,'드라마':18,'공포':27,'액션':28,'코미디':35,'역사':36,'서부':37,'스릴러':53,'범죄':80,
            '다큐멘터리':99,'SF':878,'미스터리':9648,'음악':10402,'로맨스':10749,'가족':10751,'전쟁':10752,'TV 영화':10770
        }
        genre_id = change.get(keyword)
        if Genre.objects.filter(id=genre_id).exists():
            genre = Genre.objects.filter(id=genre_id)
            ret = genre.movies.all()
            context = {
                'movies':ret,
            }
            return render(request, 'movies/index.html',context)
    return render(request,'community/nosearch.html') 