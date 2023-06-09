from paho.mqtt import client as mqtt_client
import random, time
import json
from software_design.models import Student
from software_design.serializers import StudentSerializer
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

broker = 'broker.hivemq.com'
port = 1883
pub_topic_data = "ict720/nyan/data"
client_id = f'waste-segregation-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, method):
    if method == 'POST':
        student_mac_address = Student.objects.all().values_list('student_mac_address', flat=True)
        knownBLEAddDict = {str(i): add for i, add in enumerate(student_mac_address)}
        knownBLEAddJson = json.dumps(knownBLEAddDict)
        time.sleep(1)
        result = client.publish(pub_topic_data, knownBLEAddJson)
        status = result[0]
        if status == 0:
            print(f"Send `{knownBLEAddJson}` to topic `{pub_topic_data}`")
            return True
        else:
            print(f"Failed to send message to topic {pub_topic_data}")
            return False


def run(method='POST'):
    client = connect_mqtt()
    client.loop_start()
    publish(client, method)

if __name__ == '__main__':
    run()
