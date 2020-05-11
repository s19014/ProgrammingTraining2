'''
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''


text1 = 'パトカー'
text2 = 'タクシー'


for t_1, t_2 in zip(text1, text2):
    print('{}{}'.format(t_1, t_2), end='')
print()
