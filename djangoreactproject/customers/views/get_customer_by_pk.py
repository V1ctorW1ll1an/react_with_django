from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from customers.serializers import CustomerSerializer


class GetCustomerByPk(APIView):
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)
