from asyncio import wait_for
from ctypes.wintypes import CHAR
from doctest import OutputChecker
from hashlib import new
from ipaddress import ip_address
from pydoc import describe
import time
import paramiko
import MySQLdb
import re

MH_PASS = open(" File Directory","r").read().strip()
MH_USER = " Username "
DB_PASS = open(" File Directory","r").read().strip()
# list of names from colum you want to grab IP from
hublist = ["100", "101", "102", "105", "107", "134", "135", "136", "137", "192", "193"]
num = 0
command = "adb devices" # command you want to run
commandT = "adb kill-server"
db = MySQLdb.connect(host=" IP# ", user=" USER ", passwd=DB_PASS, db = " u ")
cursor = db.cursor()
def main():
    global num
    querycommand = 'SELECT ip_address FROM mobile_hubs where mobile_hub_id =' + hublist[num]
    cursor.execute(querycommand)
    data = cursor.fetchone()
    # Converts tuple from database to string
    def convertTuple(tup):
            # initialize an empty string
        MH_IP = ''
        for item in tup:
            MH_IP = MH_IP + item
        return MH_IP
    MH_IP = convertTuple(data)

    output = ""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=MH_IP, username=MH_USER , password=MH_PASS) # connect to mh
    stdin, stdout, stderr = client.exec_command(command)
    output=stdout.read().decode('UTF-8')

    # count the amount of words containing unauthorized
    x = output.count('unauthorized')
   
    for attempt in range(5): # attempt x amount of times before breaking loop
        if x > 5:
            print("Excexuting Kill command")
            stdin, stdout, stderr = client.exec_command(commandT)
            time.sleep(3)
            stdin, stdout, stderr = client.exec_command(command)
            h = stdout.read().decode('UTF-8')
            print(h)
            x = h.count('unauthorized')
            print("attempts = ",attempt)
        else:
            print("attempts = ",attempt)
            num = num + 1
            print("Unauthorized device count = ", x)
            break
        if attempt == 4:
            print("too many attempts")
            num = num + 1
            break
        
  
for attempt in range(11):
    if num < 11:
        print("Mobile Hub Number - ", num)
        time.sleep(5)
        main()
        print("\n")
        print("\n")




