import zmq
import time

#ZeroMQのバックグラウンド・スレッドのコンテキスト
context = zmq.Context()

#このサーバは、ポート5556で待ちます
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

i = 0
while True:
    i += 1

    for topic in range(1,4):
        data = topic * i
        socket.send_string("{0} {1}".format("book/comic/kimetsu/"+str(topic), data))
        print("Topic {0} <- {1} sent".format("book/comic/kimetsu/", data))
        socket.send_string("{0} {1}".format("book/comic/gintama/"+str(topic), data))
        print("Topic {0} <- {1} sent".format("book/comic/gintama/", data))
    
    time.sleep(1)