'''
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''


import pandas as pd


DATA_FILE = 'data/popular-names.txt'


df = pd.read_csv(DATA_FILE, delimiter='\t', header=None)
print(len(df))
