import sys
import zmq

topic = "book/novel/1"

#ZeroMQのバックグラウンド・スレッドのコンテキスト
context = zmq.Context()

#このクライアントは、ポート5556に接続します(バックグラウンドにて)
socket = context.socket(zmq.SUB)
socket.connect("tcp://172.20.10.4:5556")

#チャネルの目盛りをあわせる
socket.setsockopt_string(zmq.SUBSCRIBE,topic)

while True:
    string = socket.recv_string()
    Topic,data = string.split()

    print("Topic {0} -> {1} received".format(Topic,data))