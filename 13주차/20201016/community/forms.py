from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'my-title form-control',
            'placeholder': 'Enter the title',
            'maxlength': 100,
        })
    )
    movie_title = forms.CharField(
        label='Movie title',
        widget=forms.TextInput(attrs={
            'class': 'my-title form-control',
            'placeholder': 'Enter the movie title',
            'maxlength': 50,
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'my-content form-control',
            'rows': 5,
            'cols': 50,
        })
    )
    
    class Meta:
        model = Review
        fields = ['title','movie_title', 'rank', 'content', 'image',]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'my-content form-control',
            'rows': 1,
            'cols': 50,
        })
    )

    class Meta:
        model = Comment
        fields = ['content',]
