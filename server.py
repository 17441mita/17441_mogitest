import sys
import zmq

def start_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    
    while True:
        print("Enter message:")
        message = sys.stdin.readline()
        socket.send_string(message.strip())
        
        recv_message = socket.recv_string()
        print("Receive message = %s" % recv_message)
        
    socket.close()
    context.destroy()
    
if __name__ == "__main__":
    start_server()