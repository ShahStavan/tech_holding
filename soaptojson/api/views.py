from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework import status
from .models import order

class ConvertView(APIView):
    def get(self,request,*args,**kwargs):
        result = order.objects.all()
        serializer = OrderSerializer(result, many=True)
        return Response({'status': 'success', "students":serializer.data}, status=200)
    def post(self, request):
        
        data = request.data
        # Define your conversion logic here

        # converted_data = {
        #     'order-': data['old_key'],
        #     'new_key_2': data['old_key_2'],
        # }
        # serializer = OrderSerializer(data={'data': converted_data})
        serializer = OrderSerializer(data=data)
        # format_data = {
        #     'id': data['id'],
        #     'order_id': data['order_id'],
        #     'pname': data['pname'],
        #     'product_id': data['product_id'],
        # }
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    