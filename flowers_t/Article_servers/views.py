from re import A
from Article_servers.models import article
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