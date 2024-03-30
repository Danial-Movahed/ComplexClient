import shutil
import subprocess
import socketio
import psutil
import os
import socket

sio = socketio.Client()

name = socket.gethostname()


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
            'loadAvg': format(os.getloadavg()[1] , '.2f'),
            'ram': format(psutil.virtual_memory()[2], '.1f'),
            'disk': round(100-(disk.free/disk.total * 100), 2),
            'usersCount': int(subprocess.check_output("who| awk '{print $1}'|sort -u| wc -l", shell=True).decode()),
            'packageTemp': psutil.sensors_temperatures()['coretemp'][0].current
        })
        


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('https://complexmonitor.darkube.app')
sio.wait()
