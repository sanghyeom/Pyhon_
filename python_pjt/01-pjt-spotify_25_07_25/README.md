# Spotify 아티스트 데이터 분석 프로젝트

## 1. 프로젝트 개요

본 프로젝트는 JSON 형태로 제공되는 Spotify 아티스트 데이터를 Python을 사용하여 분석하고, 요구사항에 따라 유의미한 정보를 추출 및 가공하는 것을 목표로 합니다. `pathlib`과 `json` 모듈을 활용하여 파일 시스템을 탐색하고 데이터를 처리하는 방법을 학습합니다.

## 2. 프로젝트 구조
```bash
spotify/
├── data/
│   ├── artist.json
│   ├── artists.json
│   ├── genres.json
│   └── artists/
│       ├── 116.json
│       ├── 157.json
│       └── ... (각 아티스트별 상세 정보)
├── examples/
│   ├── 01_example.py
│   ├── 02_example.py
│   ├── 03_example.py
│   └── sample.json
├── problem_a.py
├── problem_b.py
├── problem_c.py
├── problem_d.py
├── problem_e.py
├── problem_f_1.py
└── problem_f_2.py
```

-   **`data/`**: `artist.json`, `artists.json`, `genres.json`과 같이 분석에 사용될 원본 데이터 파일들이 위치합니다. `artists/` 폴더 내부에는 각 아티스트의 고유 ID를 파일명으로 하는 상세 정보 파일이 들어있습니다.
-   **`examples/`**: 데이터 처리 및 활용에 대한 예시 코드(`01_example.py`, `02_example.py`, `03_example.py`)와 샘플 데이터(`sample.json`)가 포함되어 있습니다.
-   **`problem_*.py`**: 각 문제 요구사항에 맞춰 작성된 Python 스크립트 파일들입니다.

## 3. 주요 기능 (문제 해결 스크립트)

각 `problem_*.py` 파일은 특정 목표를 달성하기 위해 작성되었습니다.

| 파일명 | 기능 설명 |
| --- | --- |
| **`problem_a.py`** | `artist.json` 파일에서 아티스트의 `id`, `name`, `images`, `type`, `genres_ids` 정보를 추출하여 새로운 딕셔너리를 생성합니다. |
| **`problem_b.py`** | `problem_a.py`의 기능에 더해, `genres.json` 파일을 참조하여 아티스트의 `genres_ids` 리스트를 실제 장르 이름으로 변환합니다. |
| **`problem_c.py`** | `artists.json`에 있는 모든 아티스트에 대해 `problem_b.py`와 동일한 로직을 적용하여, 각 아티스트의 정보를 장르명을 포함한 딕셔너리 리스트로 반환합니다. |
| **`problem_d.py`** | `artists.json`의 아티스트 ID를 기반으로 `data/artists/` 폴더 내의 각 아티스트 상세 정보 파일을 읽어, 'popularity'가 가장 높은 아티스트의 이름을 반환합니다. |
| **`problem_e.py`** | 팔로워 수가 10,000,000명을 초과하는 아티스트들의 `uri-id`와 `name` 정보를 리스트 형태로 반환합니다. |
| **`problem_f_1.py`** | 팔로워 수가 5,000,000명 초과, 10,000,000명 미만인 아티스트들의 `name`과 `followers` 정보를 리스트 형태로 반환합니다. |
| **`problem_f_2.py`**| 각 아티스트의 상세 정보 파일에서 `genres` 키를 확인하여, 'acoustic' 장르를 포함하는 아티스트의 이름을 리스트로 반환하도록 구현되어 있습니다. |

## 4. 사용 방법

각 `problem_*.py` 파일은 독립적으로 실행할 수 있습니다. 터미널에서 아래와 같이 실행하면 각 스크립트에 따른 결과가 출력됩니다.

```bash
# 예시: problem_a.py 실행
python spotify/problem_a.py

# 예시: problem_d.py 실행
python spotify/problem_d.py
```

## 5. 핵심 코드 예시
프로젝트 전반에서 사용된 주요 로직은 examples/ 폴더의 예제 코드를 통해 이해할 수 있습니다.

데이터 추출 (01_example.py): get() 메서드를 사용하여 딕셔너리에서 안전하게 값을 추출합니다. 키가 존재하지 않을 경우 None이나 지정된 기본값을 반환하여 오류를 방지합니다.

데이터 가공 (02_example.py): 원본 데이터에서 필요한 정보만 선택하고, 일부 데이터(uri)는 특정 형식에 맞게 분리하여 새로운 딕셔너리를 생성합니다.

파일 입출력 (03_example.py): pathlib으로 파일 경로를 관리하고, open 함수와 json.load()를 사용하여 JSON 파일을 Python 딕셔너리나 리스트로 변환하여 다룹니다.