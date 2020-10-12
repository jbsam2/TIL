from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


def main(request):
    return render(request,'community/main.html')

def index(request):
    return render(request,'community/index.html')

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
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
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:review_list')
    return redirect('accounts:login')


@require_POST
def like_detail(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')


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
        if get_user_model().objects.filter(username=keyword).exists():
            person = get_user_model().objects.get(username=keyword)
            context = {
                'person':person,
            }
            return render(request, 'accounts/profile.html',context)
    elif kind =='content':
        if Review.objects.filter(content__icontains=keyword).exists():
            ret = Review.objects.filter(content__icontains=keyword)
            context = {
                'reviews':ret,
            }
            return render(request, 'community/review_list.html',context)
    else:
        if Review.objects.filter(movie_title__icontains=keyword).exists():
            ret = Review.objects.filter(movie_title__icontains=keyword)
            context = {
                'reviews':ret,
            }
            return render(request, 'community/review_list.html',context)
    return render(request,'community/nosearch.html')    