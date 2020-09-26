from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    context = {
        'nums': random.sample(range(1,46),6),
    }
    return render(request, 'lotto.html', context)