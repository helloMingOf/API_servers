from django.shortcuts import render
from mqtt.models import flower_rfid
from django.http import HttpResponse
from mqtt import flowermqtt
import json

import datetime
# Create your views here.
def listjson(request):
    flower_book=flower_rfid.objects.filter(rfid_id="0xe97ecbb8").values().order_by('-time')[0:10]
    flower_book = list(flower_book)
    return HttpResponse(json.dumps(flower_book,cls=DateEncoder),"application/json")  

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

def mqttflower(requset):
    flowermqtt.publish2("flower/fan","{\"fan\":\"open\"}")
    return HttpResponse("成功")
