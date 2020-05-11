'''
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''


def cipher(target):
    target_list = []
    result = ''

    for i in range(len(target)):
        if target[i].islower():
            target_list.insert(i, chr(219-ord(target[i])))
        else:
            target_list.insert(i, target[i])

    for t in target_list:
        result += t

    return result


target = "I Am An Engineer."
print(cipher(target))
