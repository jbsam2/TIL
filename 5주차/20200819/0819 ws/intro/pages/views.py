from django.shortcuts import render

# Create your views here.
def card(request):
    context = {
        'first': ['test title1', 'test content1'],
        'second': ['test title2', 'test content2'],
        'third': ['test title3', 'test content3'],
        'fourth': ['test title4', 'test content4'],
        'fifth': ['test title5', 'test content5'],
    }
    return render(request,'card.html',context)


def community(request):
    context = {
        'first': ['#', 'Title', 'Content', 'Creation Time'],
        'second':['test title 1', 'test content 1', 'test creation time1'],
        'third':['test title 2', 'test content 2', 'test creation time2'],
        'fourth':['test title 3', 'test content 3', 'test creation time3'],
        'fifth':['test title 4', 'test content 4', 'test creation time4'],
        'sixth':['test title 5', 'test content 5', 'test creation time5'],
        'seventh':['test title 6', 'test content 6', 'test creation time6'],
    }
    return render(request,'community.html',context)