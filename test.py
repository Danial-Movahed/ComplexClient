import shutil
import subprocess
import socketio
import psutil
import os
import random
from time import sleep

sio = socketio.Client()

name = "Giv"


@sio.event
def connect():
    print('connection established')
    sio.emit('Name', {'Name': name})


@sio.on("NameAccepted")
def name_accepted():
    while True:
        disk = shutil.disk_usage("/")
        sio.emit("Monitor", {
            'name': name,
            'cpu': random.randrange(0,100),
            'loadAvg': random.randrange(0,30),
            'ram': random.randrange(0,100),
            'disk': round(disk.free/disk.total * 100, 2),
            'usersCount': random.randrange(1,9),
            'packageTemp': random.randrange(0,100)
        })
        sleep(2)
        


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:3333')
sio.wait()
