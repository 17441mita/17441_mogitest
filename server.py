import zmq
import sys

def start_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    print("Server startup.")
    while True:
        message = socket.recv_string()
        print("Received message = %s" % message)

        print("あなたの名前 サーバからクライアントへ送るメッセージ:", end='')
        message = sys.stdin.readline()
        socket.send_string(message.strip())

    socket.close()
    context.destroy()

if __name__ == "__main__":
    start_server() 