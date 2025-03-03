"""pufBackend URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from channels.routing import ProtocolTypeRouter, URLRouter
from device_detection.routing import websocket_urlpatterns
from tasks.routing import heatmap_websocket_urlpatterns
from django.core.asgi import get_asgi_application


router = routers.DefaultRouter()
# router.register(r'devices', views.DeviceView, 'device')

urlpatterns = [
    path('apii/', include(router.urls)),
    path('api/', include('puf_server.urls')),
    path('testsApi/', include('tests.urls')),
    path('uploadMeasurmentsApi/', include('upload_measurments.urls')),
    path('brokerApi/', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('deviceApi/', include('device_detection.urls'))
]

""" application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(websocket_urlpatterns)
    }
) """


""" application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(heatmap_websocket_urlpatterns)
    }
) """
