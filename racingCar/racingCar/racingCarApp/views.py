from django.template import loader, Context,RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import time, datetime, random, json
import commandOperation

__uuid_len__=20+4

def huaPageRequest(request):
    #deviceID=huaGenerateUUID()
    return render_to_response('carGame.html', context_instance=RequestContext(request))


def huaDataPost(request):
    deviceID=request.POST["deviceID"]
    scoreValue=request.POST["postData"]
    if commandOperation.commandOperation(deviceID, scoreValue):
        return HttpResponse(" Succeed!")
    else:
        return HttpResponse(" Error Happened!")

