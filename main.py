import shutil
import subprocess
import socketio
import psutil
import os
import random

sio = socketio.Client()

name = "Rostam"


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
            'cpu': psutil.cpu_percent(0.5),
            'loadAvg': random.randint(0,20),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': random.randint(0,100),
            'packageTemp': random.randint(0,100)
        })
        sio.emit("Monitor", {
            'name': "Giv",
            'cpu': random.randint(0,100),
            'loadAvg': random.randint(0,20),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': random.randint(0,100),
            'packageTemp': random.randint(0,100)
        })
        sio.emit("Monitor", {
            'name': "Esfandiar",
            'cpu': random.randint(0,100),
            'loadAvg': random.randint(0,20),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': random.randint(0,100),
            'packageTemp': random.randint(0,100)
        })
        sio.emit("Monitor", {
            'name': "Piran",
            'cpu': random.randint(0,100),
            'loadAvg': random.randint(0,20),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': random.randint(0,100),
            'packageTemp': random.randint(0,100)
        })
        sio.emit("Monitor", {
            'name': "Roudabeh",
            'cpu': random.randint(0,100),
            'loadAvg': random.randint(0,20),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': random.randint(0,100),
            'packageTemp': random.randint(0,100)
        })


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:3333')
sio.wait()
