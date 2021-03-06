"""flowers_t URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from Login_servers import views as User_views
from Article_servers import views as Aricle_views
from mqtt import views as mqtt_viwes
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', User_views.login_view),
    path('updateperson/',User_views.updateperson_view),
    path('register/',User_views.register_view),
    path('picture/',User_views.flie_images_view),
    path('articles/',Aricle_views.listjson_view),
    path('add_article/',Aricle_views.add_listjson),
    path('flower_book/',Aricle_views.listjson_bookview),
    path('flower_rfid/',mqtt_viwes.listjson),
    path('mqttpublish/',mqtt_viwes.mqttflower),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
