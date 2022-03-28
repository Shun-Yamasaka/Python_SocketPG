# -*- coding: utf-8 -*-
"""
client0.pyプログラム
Pythonによるクライアントソケットの利用例
50000番ポートでサーバに接続
使用方法
> python3 client0.py
"""

# モジュールのインポート
import socket

# グローバル変数
HOST = "localhost" # 接続先ホストの名前
#HOST = "127.0.0.1" # 接続先ホストの名前
PORT = 50000 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))
# サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# コネクションのクローズ
client.close()
# client0.pyの終わり
