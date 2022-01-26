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
        socket.send_string("{0} {1}".format("book/comic/"+str(topic),data))
        print("Topic {0} <- {1} sent".format("book/comic/",data))
        socket.send_string("{0} {1}".format("book/novel/"+str(topic),data))
        print("Topic {0} <- {1} sent".format("book/novel/",data))

    time.sleep(1)