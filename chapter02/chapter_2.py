import requests


DATA_FILE = "https://nlp100.github.io/data/popular-names.txt"


get_url_info = requests.get(DATA_FILE)
print(get_url_info.text)


# python3 chapter_2.py > data/popular-names.txt　でテキストファイル作成
