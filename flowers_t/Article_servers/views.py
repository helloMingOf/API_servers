from re import A
from Article_servers.models import article
from Article_servers.models import flower_book1
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def listjson_view(request):
    articles=article.objects.all().values()
    articles = list(articles)
    return HttpResponse(json.dumps(articles),"application/json")

@csrf_exempt
def add_listjson(request):
    if request.method == 'POST':
        author=request.POST.get('author')
        time=request.POST.get('time')
        text=request.POST.get('text')
        picture=request.POST.get('picture')
        article.objects.create(author=author,time=time,text=text,picture=picture)
        return HttpResponse('文章上传成功!')
    else:
        return HttpResponse('GET请求无效')  

def listjson_bookview(request):
    flower_book=flower_book1.objects.all().values()
    flower_book = list(flower_book)
    return HttpResponse(json.dumps(flower_book),"application/json")  