import requests
from django.shortcuts import render


class URLMaker:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = ''


    def __init__(self, key):
        self.key = key


    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'   



def get_movie_cd(title):
    url_maker = URLMaker('9b416041e07567eeca14ecbfa2d95cb2')
    url = url_maker.get_url('movie', 'searchMovieList')

    payload = {
        'movieNm' : title,
    }
    
    movie_dict = requests.get(url, params=payload).json()
    movie_info = movie_dict.get('movieListResult').get('movieList')

    return movie_info[0]['openDt'][:4]

def search(request):
    return render(request,'search-movie.html')

def info(request):
    title = request.GET.get('name')
    year = get_movie_cd(title)
    context = {
        'title': title,
        'year':year,
    }
    return render(request,'info.html', context)