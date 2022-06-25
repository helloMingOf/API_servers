# 为了能在外部脚本中调用Django ORM模型，必须配置脚本环境变量，将脚本注册到Django的环境变量中
import os, sys
import django
# 第一个参数固定，第二个参数是工程名称.settings
os.environ.setdefault('DJANGO_SETTING_MODULE', 'flowers_t.settings')
django.setup()
from mqtt.models import flower_rfid
from mqtt.models import flower
# 引入mqtt包
import paho.mqtt.client as mqtt
# 使用独立线程运行
from threading import Thread
from mqtt import models

import time
import json


# 建立mqtt连接
def on_connect(client, userdata, flag, rc):
    print("Connect with the result code " + str(rc))
    client.subscribe('flower/#', qos=2)

# 接收、处理mqtt消息
def on_message(client, userdata, msg):
    out = str(msg.payload.decode('utf-8'))
    print(msg.topic)
    print(out)
    out = json.loads(out)

    # 收到消息后执行任务
    if msg.topic == 'flower/uid':
        print(out['uid'])
        flower1=flower.objects.get(id=out['uid'])
        flower_rfid.objects.create(rfid_id=flower1.id,flower_name=flower1.flower_name)



# mqtt客户端启动函数
def mqttfunction():
    global client
    # 使用loop_start 可以避免阻塞Django进程，使用loop_forever()可能会阻塞系统进程
    # client.loop_start()
    #client.loop_forever() 有掉线重连功能
    client.loop_forever(retry_first_connection=True)


client = mqtt.Client(client_id="test", clean_session=False)

# 启动函数
def mqtt_run():
    client.on_connect = on_connect
    client.on_message = on_message
    # 绑定 MQTT 服务器地址
    broker = '120.79.130.114'
    # MQTT服务器的端口号
    client.connect(broker, 1883, 62)
    client.username_pw_set('zjm', '123456')
    client.reconnect_delay_set(min_delay=1, max_delay=2000)
    # 启动
    mqttthread = Thread(target=mqttfunction)
    mqttthread.start()


# 启动 MQTT
# mqtt_run()


if __name__ == "__main__":
    mqtt_run()

def publish2(totic,mesage):
    client.publish(topic=totic,payload=mesage,qos=0)