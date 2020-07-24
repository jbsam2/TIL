import json

def music_info(music):
    ret = {}
    ret['singer'] = music['singer']
    ret['title'] = music['title']
    return ret

#json 파일을 불러오는 코드
music_json = open('data/music.json', encoding='UTF8')
#json을 dict으로 변환하는 코드
music_dict = json.load(music_json)

#실행
music_info(music_dict)