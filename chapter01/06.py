'''
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYと
して求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXお
よびYに含まれるかどうかを調べよ．
'''

text1 = 'paraparaparadise'
text2 = 'paragraph'


def bi_gram(text):
    character_list = []  # 文字bi-gram

    character = ''.join(text.split())
    for i in range(len(character)-1):
        character_list.append(character[i:i+2])

    return character_list


# def se_in(target, s):
#     '''
#     targetに"se"が含まれているかの関数
#     sは変数名
#     '''
#     set_target = set(target)
#     if 'se' in set_target:
#         return '{}にseは含まれている'.format(s)
#     else:
#         return '{}にseは含まれていない'.format(s)


X, Y = bi_gram(text1), bi_gram(text2)
set_X = set(X)
set_Y = set(Y)

XY_union = set_X | set_Y  # 和集合
XY_intersection = set_X & set_Y  # 　積集合
XY_difference = set_X - set_Y   # 差集合


print('X: {}'.format(set_X))
print('Y: {}'.format(set_Y))
print('和集合: {}'.format(XY_union))
print('積集合: {}'.format(XY_intersection))
print('差集合: {}'.format(XY_difference))
# print(se_in(set_X, 'X'))
# print(se_in(set_Y, 'Y'))
