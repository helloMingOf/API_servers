from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from Login_servers.models import User
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login_view(request):
    if request.method=='POST':
        myID=request.POST.get('uid')
        mypassword=request.POST.get('password')
        try:
            count = User.objects.filter(ID=myID).count()
            if count == 0:
                date_error = {
                    'status': '-1',
                    'Status Code': 404
                }
                return HttpResponse(json.dumps(date_error), content_type='application/json')
            user=User.objects.get(ID=myID)
            if user.password==mypassword:
                data={
                    'ID': user.ID,
                    'name': user.name,
                    'password': user.password,
                    'region': user.region,
                    'birthday':user.birthday,
                    'picture': user.picture,
                    'gender': user.gender,
                    'status': '1',
                    'Status Code': 200
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                date_error = {
                    'status': '-2',
                    'Status Code': 404
                }
                return HttpResponse(json.dumps(date_error), content_type='application/json')
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(date_error),content_type='application/json')
    else:
        return HttpResponse('GET请求无效')
@csrf_exempt
def updateperson_view(request):
    if request.method == 'POST':
        ID=request.POST.get('uid')
        name=request.POST.get('name')
        region=request.POST.get('region')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        picture=request.POST.get('picture')
        User.objects.filter(ID=ID).update(name=name,region=region,gender=gender,birthday=birthday)
        date = {
            'status': '1',
            'Status Code': 200
        }
        return HttpResponse(json.dumps(date), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')