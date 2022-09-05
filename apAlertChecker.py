from doctest import OutputChecker
from hashlib import new
from ipaddress import ip_address
from pydoc import describe
import time
import paramiko
import MySQLdb
import re
MH_PASS = open("/opt/cbt/cbt_env/cbthpass","r").read().strip()
MH_USER = "cbtadmin"
DB_PASS = open("/opt/cbt/cbt_env/cbtdbpassword","r").read().strip()

command1 = "dns-sd -B '_airplay'"
db = MySQLdb.connect(host="10.191.1.11", user="web", passwd=DB_PASS, db = "cbt")
cursor = db.cursor()


def main():
    querycommand = "Select ip_address as MH_IP from mobile_hubs where ip_address LIKE '%133%'; "
    print(querycommand)
    cursor.execute(querycommand)
    # data = cursor.fetchall()
    # # Converts tuple from database to string
    # def convertTuple(tup):
    #         # initialize an empty string
    #     MH_IP = ""
    #     for item in tup:
    #         MH_IP = 
    #     return MH_IP
    # MH_IP = convertTuple(data)

    for items in cursor.fetchall():
        ite = items[0]
        strr = ''.join(ite)

    x = list(ite)
        # print(strr)

    # data = cursor.fetchall()
    
    print(x, type(x))

        

    # output = ""
    # client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # client.connect(hostname=MH_IP, username=MH_USER , password=MH_PASS) # connect to mobile hub
    # stdin, stdout, stderr = client.exec_command(command1)
    # output=stdout.read().decode('UTF-8')
    
main()
