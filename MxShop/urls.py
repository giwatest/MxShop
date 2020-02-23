"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
#from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
#drf文档
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('goods', GoodsListViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),  #图片资源路由
    #path('goods/', GoodsListView.as_view(), name="goods-list"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/',include_docs_urls(title='暮雪生鲜')),
]
