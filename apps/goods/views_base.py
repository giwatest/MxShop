# encoding:utf-8
__autor__ = 'GIWA'

from django.views.generic.base import View
from goods.models import Goods
import json
from django.core import serializers

class GoodsListView(View):
    def get(self, request):

        goods = Goods.objects.all()[:10]
        #方法1:
        # json_list = []
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        #方法2:
        # from django.forms.models import model_to_dict
        # json_list = []
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        #方法3:
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import JsonResponse
        return JsonResponse(json_data, safe=False)