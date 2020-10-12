from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:review_list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:review_list')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html',context)


@require_POST
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user.is_authenticated:        
        user = request.user
        if user != person:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
            else:
                person.followers.add(user)
        return redirect('accounts:profile', person.username)
    else:
        return redirect('accounts:profile', person.username)