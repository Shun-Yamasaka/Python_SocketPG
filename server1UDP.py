# -*- coding: utf-8 -*-
"""
server1UDP.pyプログラム
Pythonによるサーバソケットの利用例（UDP版）
50000番ポートで接続を待ち受けて、時刻を返します
接続時にコンソールにメッセージを出力します
ctrl+Breakで終了します
使用方法
> python3 server1UDP.py
"""

# モジュールのインポート
import socket
import datetime

# グローバル変数
PORT = 50000 # ポート番号
BUFSIZE = 4096 # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# アドレスの設定
server.bind(("", PORT))

# クライアントへの対応処理
while True:                                 # 対応の繰り返し
    data, client = server.recvfrom(BUFSIZE) # 通信用ソケットの取得
    msg = str(datetime.datetime.now())      # メッセージの作成
    server.sendto(msg.encode("UTF-8"))     # メッセージの送信
    print(msg, "接続要求あり")
    print(client)
# server1UDP.pyの終わり