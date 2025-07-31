import json
from pprint import pprint

def artist_info(artist):
    re_artist={}
    # re_artist['genres_ids'] = artist['genres_ids']
    # re_artist['id'] = artist['id']
    # re_artist['images'] = artist['images']
    # re_artist['name'] = artist['name']
    # re_artist['type'] = artist['type']
    choice = ['genres_ids','id','images','name','type']
    for i in choice :
        re_artist[i] = artist[i]

    return re_artist
    
    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))


