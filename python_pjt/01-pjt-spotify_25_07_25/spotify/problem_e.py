import json
from pprint import pprint


    
def dec_artists(artists):
    checks_id =[]
    for artist in artists :
        checks_id.append(artist['id'])
    
    artists_file = []
    for check_id in checks_id :
        artist_file = {}
        file_name = str(check_id)+'.json'
        current_dir = Path(__file__).resolve().parent
        artist = open(current_dir / 'data' / 'artists' / file_name , encoding='utf-8')
        artist_detail = json.load(artist)

        artist_file['uri-id'] = artist_detail['uri'][15:]
        artist_file['name'] = artist_detail['name']
        artist_file['followers'] = artist_detail['followers']['total']
        artists_file.append(artist_file)
    
    pop_aritsts = []
    for artist in artists_file:
        if artist['followers'] > 10000000  :
            del artist['followers']
           
            pop_aritsts.append(artist)


    return pop_aritsts

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    pprint(dec_artists(artists_list))


