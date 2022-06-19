
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from Login_servers.models import User
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login_view(request):#登录
    if request.method=='POST':
        myID=request.POST.get('uid')
        mypassword=request.POST.get('password')
        try:
            count = User.objects.filter(ID=myID).count()
            if count == 0:
                date_error = {
                    'status': '-1',
                    'Status Code': 404,
                    'message':'用户不存在'
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
                    'picture':str(user.picture),
                    'gender': user.gender,
                    'status': '1',
                    'Status Code': 200,
                    'message':'登录成功'
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                date_error = {
                    'ID':myID,
                    'status': '-2',
                    'Status Code': 404,
                    'message':'密码错误'
                }
                return HttpResponse(json.dumps(date_error), content_type='application/json')
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(date_error),content_type='application/json')
    else:
        return HttpResponse('GET请求无效')
@csrf_exempt
def updateperson_view(request):#更新个人信息
    if request.method == 'POST':
        ID=request.POST.get('uid')
        name=request.POST.get('name')
        region=request.POST.get('region')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        User.objects.filter(ID=ID).update(name=name,region=region,gender=gender,birthday=birthday)
        date = {
            'status': '1',
            'Status Code': 200
        }
        return HttpResponse(json.dumps(date), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')
@csrf_exempt
def register_view(request):#注册
    if request.method == 'POST':
        ID=request.POST.get('uid')
        name=request.POST.get('name')
        region=request.POST.get('region')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        picture=request.POST.get('picture')
        password=request.POST.get('password')
        count = User.objects.filter(ID=ID).count()
        if count ==1:
            date_error = {
                'status': '-1',
                'Status Code': 404,
                'message': '用户已存在'
            }
            return HttpResponse(json.dumps(date_error), content_type='application/json')
        User.objects.create(ID=ID,name=name,region=region,gender=gender,birthday=birthday,password=password,picture=picture)
        date = {
            'status': '1',
            'Status Code': 200,
            'message': '注册成功！'
        }
        return HttpResponse(json.dumps(date), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')

@csrf_exempt
def flie_images_view(request):
    if request.method == 'POST':
        ID=request.POST.get('uid')
        img = User.objects.get(ID=ID)
        img.picture=request.FILES.get('img')
        img.save()
    return HttpResponse('图片上传成功!')
