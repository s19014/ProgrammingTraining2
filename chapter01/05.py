'''
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''


text = 'I am an NLPer'


def bi_gram(text):
    word_list = []  # 単語bi-gram
    character_list = []  # 文字bi-gram

    for i in range(len(text) - 1):
        word_list.append(text[i:i+2])

    character = text.split(' ')
    for i in range(len(character) - 1):
        character_list.append('{} {}'.format(character[i], character[i+1]))

    return word_list, character_list


result = bi_gram(text)
for r in result:
    print(r)
