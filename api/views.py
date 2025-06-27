from django.http.response import JsonResponse

from api.models import Product
from api.serializers import ProductSerializer


def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({
        'data': serializer.data
    })
