from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer


class DeleteCustomer(APIView):
    def delete(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
