'''
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
'''


x = 12
y = "気温"
z = 22.4


def temperature(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)


print(temperature(x=x, y=y, z=z))
