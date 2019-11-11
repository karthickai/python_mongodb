import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
db = myclient.iotb


def validate(data):
    users = db.users.find()
    for user in users:
        if user[_id] == data["clientId"]:
            print("Authorised")
            break
    print("Unauthorised")


import paho.mqtt.client as mqtt
import json


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    data = json.loads(m_decode)
    validate(data)


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("/iotb/request", 0)

mqttc.loop_forever()