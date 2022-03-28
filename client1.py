# -*- coding: utf-8 -*-
"""
client1.pyプログラム
Pythonによるクライアントソケットの利用例
50000番ポートで指定したサーバに接続します
接続後、サーバにメッセージを送ります
使用方法
> python3 client1.py
"""

# モジュールのインポート
import socket
import sys

# グローバル変数
PORT = 50000 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
host = input("接続先サーバ：")
try:
    client.connect((host, PORT))
except:
    print("接続できません")
    sys.exit()
# サーバへのメッセージの送信
msg = input("メッセージを入力：")
client.sendall(msg.encode("utf-8"))
# サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print("サーバからのメッセージ：")
print(data.decode("UTF-8"))
# コネクションのクローズ
client.close()
# client1.pyの終わり
