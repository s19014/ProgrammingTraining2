'''
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''


text = 'I am an NLPer'


def bi_gram(text):
    word_list = []  # 単語bi-gram
    character_list = []  # 文字bi-gram

    word = text.split()
    for i in range(len(word) - 1):
        word_list.append(word[i:i+2])

    character = ''.join(text.split())
    for i in range(len(character)-1):
        character_list.append(character[i:i+2])

    return word_list, character_list


print(bi_gram(text))
