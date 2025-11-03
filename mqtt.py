import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

def publish(topic, msg):
    client.publish(topic, msg)
