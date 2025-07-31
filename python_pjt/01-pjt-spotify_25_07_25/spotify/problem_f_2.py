import json
from pathlib import Path
from pprint import pprint


def acoustic_artists(artists_list, genres_list):
    """
    B. 장르에 acoustic이 포함된 아티스트의 이름을 추출하는 함수
    (수정된 로직)
    """
    # 1. genres_list에서 'acoustic' 장르의 id를 찾습니다.
    acoustic_genre_id = None
    for genre in genres_list:
        if genre['name'] == 'acoustic':
            acoustic_genre_id = genre['id']
            break  # 찾았으면 더 이상 반복할 필요가 없습니다.

    # 'acoustic' 장르가 genres.json에 없으면 빈 리스트를 반환합니다.
    if acoustic_genre_id is None:
        return []

    # 2. artists_list를 순회하며 acoustic_genre_id를 가진 아티스트를 찾습니다.
    acoustic_artist_names = []
    for artist in artists_list:
        # artist 딕셔너리에 'genres_ids' 키가 없을 경우를 대비해 .get() 사용
        if acoustic_genre_id in artist.get('genres_ids', []):
            acoustic_artist_names.append(artist['name'])

    return acoustic_artist_names


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    current_dir = Path(__file__).resolve().parent

    # artists.json과 genres.json 파일을 모두 읽어옵니다.
    with open(current_dir / 'data' / 'artists.json', encoding='utf-8') as f_artists:
        artists_list = json.load(f_artists)

    with open(current_dir / 'data' / 'genres.json', encoding='utf-8') as f_genres:
        genres_list = json.load(f_genres)

    # 수정된 함수에 두 개의 리스트를 모두 전달합니다.
    pprint(acoustic_artists(artists_list, genres_list))