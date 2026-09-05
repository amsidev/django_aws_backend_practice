from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({
                'data': serializer.data,
                'message': 'Orders data fetched sucessfully'
            }, status = status.HTTP_200_OK)
        except:
            return Response({
                'data': {},
                'message': 'Something went wrong while fetching the data'
            }, status = status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.s_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong while fetching the data'
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'New order is created or Placed successfully'
            }, status = status.HTTP_201_CREATED)
        
        except:
            return Response({
                'data': {},
                'message': 'Something went wrong while creating the order'
            }, status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try: 
            data = request.data
            order = Order.object.filter(id = data.get('id'))

            if not order.exists():
                return Response({
                    'data': {},
                    'message': 'Order does not exists'
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer = OrderSerializer(order[0], data = data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong while updating the order'
                }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Order updated successfully'
            }, status = status.HTTP_200_OK)

        except:
            return Response({
                'data': {},
                'message': 'Something went wrong while updating the order'
            }, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id = data.get('id'))

            if not order.exists():
                return Response({
                    'data': {},
                    'message': 'Order does not exists'
                }, status = status.HTTP_404_NOT_FOUND)

            order[0].delete()
            return Response({
                'data': {},
                'message': 'Order deleted successfully'
            }, status = status.HTTP_200_OK)

        except:
            return Response({
                'data': {},
                'message': 'Something went wrong while deleting the order'
            }, status = status.HTTP_400_BAD_REQUEST)