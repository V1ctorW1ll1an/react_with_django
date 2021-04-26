from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from customers.serializers import CustomerSerializer


class GetAllCustomers(APIView):
    def get(self, request):
        data = []
        next_page = 1
        previous_page = 1
        customers = Customer.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CustomerSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages,
                         'nextlink': '/api/customers/?page=' + str(next_page),
                         'prevlink': '/api/customers/?page=' + str(previous_page)})
