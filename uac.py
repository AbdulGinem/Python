import subprocess
import time
from tkinter import *
import os

cmd = "adb shell input keyevent 26" # power button
cmd2 = "adb shell input keyevent 82" # unlocks phone
cmd3 = "adb shell input keyevent KEYCODE_HOME" # home button
cmd4 = "adb shell am start -a android.settings.SETTINGS" # settings
cmd5 = "adb shell pm disable-user --user 0 com.sec.android.app.camera" # disable Camera
cmd6 = "adb shell pm enable com.sec.android.app.camera" # enable camera
cmd7 = "adb shell reboot" # reboot device
cmd8 = "scrcpy -m500" # launch scrcpy
cmd9 = "adb shell dumpsys battery" # battery stat
cmd10 = "adb shell getprop ro.product.model" # model 
cmd11 = "adb shell getprop ro.build.version.release" # version



# "adb shell pm clear com.lge.camera" kill app with package name
# adb shell pm disable-user --user 0 com.sec.android.app.camera Disable Camera
# adb shell pm enable com.sec.android.app.camera  Enable Camera
# adb shell dumpsys activity - seee surrent avtivity
# adb shell getprop ro.product.model - model
# adb shell getprop ro.build.version.release - android version

def click():
    a = subprocess.Popen(cmd, shell=True)

def click2():
    b = subprocess.Popen(cmd2, shell=True)

def click3():
    c = subprocess.Popen(cmd3, shell=True)

def click4():
    d = subprocess.Popen(cmd4, shell=True)

def click5():
    e = subprocess.Popen(cmd5, shell=True)

def click6():
    f = subprocess.Popen(cmd6, shell=True)  

def click7():
    g = subprocess.Popen(cmd7, shell=True)

def click8():
    g = subprocess.Popen(cmd8, shell=True)    

def click9():
    g = subprocess.Popen(cmd9, shell=True)

def click10():
    g = subprocess.Popen(cmd10, shell=True)

def click11():
    g = subprocess.Popen(cmd11, shell=True)          



window = Tk()



window.title("Samsung ADB Shell Buttons")
window.geometry("500x500")
my_frame = Frame(window, width=500, height=500)
my_frame.pack(fill=BOTH, expand=True)
health = Label(window, text = "Health =", fg='blue').place(x=260,y=65)
level = Label(window, text = "Level =", fg='blue').place(x=260,y=80)
temperature = Label(window, text = "Temperature =", fg='blue').place(x=260,y=95)
current = Label(window, text = "current =", fg='blue').place(x=260,y=110)


button1 = Button(my_frame, text='Power Button', highlightbackground='grey')
button2 = Button(window, text='Unlock', highlightbackground='grey')
button3 = Button(window, text='Home Button', highlightbackground='grey')
button4 = Button(window, text='Settings', highlightbackground='grey')
button5 = Button(window, text='Disable Camera', highlightbackground='grey')
button6 = Button(window, text='Enable Camera', highlightbackground='grey')
button7 = Button(window, text='Reboot Device', highlightbackground='grey')
button8 = Button(window, text='Launch Scrcpy', highlightbackground='grey')
button9 = Button(window, text='Battery Status', highlightbackground='grey')
button10 = Button(window, text='Model Number', highlightbackground='grey')
button11 = Button(window, text='Android Version', highlightbackground='grey')

button1.config(command=click)
button2.config(command=click2)
button3.config(command=click3)
button4.config(command=click4)
button5.config(command=click5)
button6.config(command=click6)
button7.config(command=click7)
button8.config(command=click8)
button9.config(command=click9)
button10.config(command=click10)
button11.config(command=click11)



button1.place(x=0, y=0, width=100, height=50)
button2.place(x=0, y=70, width=100, height=50)
button3.place(x=0, y=140, width=100, height=50)
button4.place(x=0, y=210, width=100, height=50)
button5.place(x=0, y=280, width=100, height=50)
button6.place(x=0, y=350, width=100, height=50)
button7.place(x=0, y=420, width=100, height=50) 
button8.place(x=150, y=0, width=100, height=50) 
button9.place(x=150, y=70, width=100, height=50)    
button10.place(x=150, y=140, width=100, height=50)  
button11.place(x=150, y=210, width=100, height=50)    



window.mainloop()



# a = subprocess.Popen(cmd, shell=True)
# time.sleep(2)
# b = subprocess.Popen(cmd2, shell=True)
# time.sleep(2)
# c = subprocess.Popen(cmd3, shell=True)
# time.sleep(2)
# d = subprocess.Popen(cmd4, shell=True)
# time.sleep(2)
# d = subprocess.Popen(cmd5, shell=True)


