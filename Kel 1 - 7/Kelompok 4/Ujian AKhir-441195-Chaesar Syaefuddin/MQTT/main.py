from tkinter import *
from paho.mqtt import client as mqtt_client

# MQTT
broker = '10.33.162.50'
port = 1883
topic4 = "esp32/4"
topic5 = "esp32/5"
topic_sub = "esp32/status"
# generate client ID with pub prefix randomly
client_id = 'your client id'
username = 'UGM-Hotspot'
password = ''
deviceId = "your deviceId"
 
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)
 
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
 
def publish4(client, status):
    result = client.publish(status,topic4)
    msg_status = result[0]
    if msg_status ==0:
        print(f"message : {status} sent to topic {topic4}")
    else:
        print(f"Failed to send message to topic {topic4}")

def publish5(client, status):
    result = client.publish(status,topic5)
    msg_status = result[0]
    if msg_status ==0:
        print(f"message : {status} sent to topic {topic5}")
    else:
        print(f"Failed to send message to topic {topic5}")
 
 
# def subscribe(client: mqtt_client):
#     def on_message(client, userdata, msg):
#         print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
#         # y = json.loads(msg.payload.decode())
#         # temp = y["notification"]["parameters"]["temp"]
#         # hum = y["notification"]["parameters"]["humi"]
#         # print("temperature: ",temp,", humidity:",hum)
 
 
 
#     client.subscribe(topic_sub)
#     client.on_message = on_message

# MQTT End

# GUI
root = Tk()
root.title("Ujian Teknik Kendali - MQTT ESP32")
root.geometry("500x800")


# Switch image
on = PhotoImage(file=".Yeyen/MQTT/images/on.png")
off = PhotoImage(file=".Yeyen/MQTT/images/off.png")

# LED 1
global led4_is_on
led4_is_on = True

led4_label = Label(root, text="Led 1 Switch is On!")
led4_label.pack(pady=20)

def led1_switch():
    global led4_is_on
    if led4_is_on:
        led4_btn.config(image=off)
        led4_label.config(text="Led 1 Switch is Off!")
        publish4(client,"0")
        led4_is_on = False
    else:
        led4_btn.config(image=on)
        led4_label.config(text="Led 1 Switch is On!")
        publish4(client,"1")
        led4_is_on = True

led4_btn = Button(root, image=on, bd=0, command=led1_switch)
led4_btn.pack(pady=50)

# LED 2
led5_label = Label(root, text="Led 2 Switch is On!")
led5_label.pack(pady=20)

def led2_switch():
    global led5_is_on
    if led5_is_on:
        led5_btn.config(image=off)
        led5_label.config(text="Led 1 Switch is Off!")
        publish5(client,"0")
        led5_is_on = False
    else:
        led5_btn.config(image=on)
        led5_label.config(text="Led 1 Switch is On!")
        publish5(client,"1")
        led5_is_on = True

led5_btn = Button(root, image=on, bd=0, command=led2_switch)
led5_btn.pack(pady=50)

# GUI End

# Start Program
client = connect_mqtt()
# subscribe(client)
client.loop_start()
 
 
root.mainloop()
client.loop_stop()