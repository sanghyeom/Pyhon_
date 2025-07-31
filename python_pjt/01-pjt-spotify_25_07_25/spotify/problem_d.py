import json
from pprint import pprint

    
def max_popularity(artists):
    checks_id =[]
    choice = ['id']
    for artist in artists :
        re_artist={}
        for i in choice :
           checks_id.append(artist[i])



    max_popular = {}
    max_pop = []
    result = ''

    for check_id in checks_id :
        file_name = str(check_id)+'.json'
        current_dir = Path(__file__).resolve().parent
        artist = open(current_dir / 'data' / 'artists' / file_name , encoding='utf-8')
        artist_detail = json.load(artist)
        max_popular[artist_detail['name']]=artist_detail['popularity']
    
    for i in max_popular :
        max_pop.append(max_popular[i])
    
    for j in max_popular :
        if max_popular[j] == max(max_pop) :
            result = j
            
    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))
