'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の
文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単
語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could
actually understand what I was reading : the phenomenal power of the human mind .”）
を与え，その実行結果を確認せよ．
'''


import random


text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
text2 = 'I like an aplle'


def reordering(text):
    len_text = len(text)
    if len_text <= 4:
        return text
    else:
        text_list = text.split()
        text_first = text_list.pop(0)
        text_last = text_list.pop(-1)
        random.shuffle(text_list)
        text_list.insert(0, text_first)
        text_list.append(text_last)
        text_shuffle = " ".join(text_list)
        return text_shuffle


print("4文字以上")
print(reordering(text))
print("\n4文字以下")
print(reordering(text2))
