'''
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also 
Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に
2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
'''


text = '''Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'''
text_list = text.split()

answer = {}
for index, word in enumerate(text_list, 1):
    if index in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        answer[index] = word[0]
    else:
        answer[index] = word[:2]

print(answer)
