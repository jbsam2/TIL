import json
import pprint

def music_info(musics):
    ret = []
    for music in musics:
        tmp = {}
        tmp['singer'] = music['singer']
        tmp['title'] = music['title']
        ret = ret + [tmp]
    return ret


#한글 때문에 encoding 해줘야 됨
musics_json = open('data/musics.json',encoding='UTF8')
musics_list = json.load(musics_json)

pprint.pprint(musics_info(musics_list))