'''
“Now I need a drink, alcoholic of course, after the heavy lectures involving 
quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数
を先頭から出現順に並べたリストを作成せよ．
'''


import re


text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
text_list = re.split('\W+', text)
text_list.pop()

word_count = []
for word in text_list:
    word_count.append(len(word))

print(word_count)
