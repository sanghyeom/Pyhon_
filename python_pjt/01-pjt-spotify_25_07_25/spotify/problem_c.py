import json
from pprint import pprint


def artist_info(artists,genres):
    re_artists=[]
    choice = ['genres_ids','id','images','name','type']
    for artist in artists :
        re_artist={}
        for i in choice :
           re_artist[i] = artist[i]

        for genre in genres:
            for j in re_artist['genres_ids']:
                if j == genre.get('id') :
                    re_artist['genres_ids'][re_artist['genres_ids'].index(j)]=genre.get('name')
        re_artists.append(re_artist)
    return re_artists
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
