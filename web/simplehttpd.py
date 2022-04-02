# -*- coding: utf-8 -*-
"""
simplehttpd.pyプログラム
Webサーバプログラム
8080番ポートでHTTP接続を待ち受けます
Ctrl+Breakで終了します
使い方: >python3 simplehttpd.py
"""

# モジュールのインポート
import http.server
from turtle import ht

# グローバル変数
PORT = 8080 # ポート番号

# メイン実行部
# 事前設定
handlerclass = http.server.SimpleHTTPRequestHandler
simpled = http.server.HTTPServer(("", PORT), handlerclass)
# サーバの実行
simpled.serve_forever()
# simplehttpd.py End