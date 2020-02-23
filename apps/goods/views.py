
# Create your views here.

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页,分页,搜索,过滤,排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'goods_brief']
    search_fields = ['name', 'goods_brief']
    ordering_fields = ['sold_num', 'shop_price']


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
