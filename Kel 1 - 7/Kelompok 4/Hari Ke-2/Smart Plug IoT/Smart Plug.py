from pyHS100 import SmartPlug
from pprint import pformat as pf
from tkinter import *

window_main = Tk(className='Smart Plug Control Switch',)
window_main.geometry("400x200")

plug = SmartPlug("192.168.0.1") # data IP dari rotter utama device yang dimana bisa membaca dari wireless properties bisa diganti sesuai yang terbaca, untuk manualnya bisa menggunakan code discover device secara terpisah dari thonny
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device
print("Current state: %s" % plug.state)
plug.turn_off()
plug.turn_on()


plug.state = "ON"
print("Current state: %s" % plug.state)

print("Current LED state: %s" % plug.led)
plug.led = True # turn off led
print("New LED state: %s" % plug.led)

def plugFunctionON() :
    plug.state = "ON"
def plugFunctionOFF() :
    plug.state = "OFF"
def close():
    window_main.destroy()

myButton1 = Button(window_main, text="Plug ON", command=plugFunctionON)
myButton1.config(width=20, height=2)
myButton2 = Button(window_main, text="Plug OFF",command=plugFunctionOFF)
myButton2.config(width=20, height=2)
myButton3 = Button(window_main, text="Exit",command=close)
myButton3.config(width=20, height=2)
myButton1.pack()
myButton2.pack()
myButton3.pack()

window_main.mainloop()