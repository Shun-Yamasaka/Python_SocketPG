# -*- coding: utf-8 -*-
"""
urlopen.pyプログラム
指定したURLからHTMLファイルを取得します
使い方: >python3 urlopen.py
"""

# モジュールのインポート
import urllib.request

# グローバル変数
DURL = "http://localhost:8080/"

# メイン実行部
# 取得先URLの設定
url = input("取得先URL:")
if url == "": # デフォルトのURLを設定
    url = DURL
# 文字コードの設定
chcode = input("文字コード:")
if chcode == "": # デフォルトの文字コード設定
    chcode = "UTF-8"
# URLを開く
urlinfo = urllib.request.urlopen(url)
# HTMLファイルを取得する
html = urlinfo.read()
# 画面出力
print(html.decode(chcode))
# urlopen.py End