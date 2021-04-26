"""djangoreactproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from customers.views import create_customer, update_customer, get_all_customers, get_customer_by_pk, delete_customer
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/customers/getall/$', get_all_customers.GetAllCustomers.as_view()),

    url(r'^api/customers/create/$', create_customer.CreateCustomer.as_view()),
    url(r'^api/customers/update/(?P<pk>[0-9]+)/$', update_customer.UpdateCustomer.as_view()),

    url(r'^api/customers/getbypk/(?P<pk>[0-9]+)/$', get_customer_by_pk.GetCustomerByPk.as_view()),
    url(r'^api/customers/delete/(?P<pk>[0-9]+)/$', delete_customer.DeleteCustomer.as_view()),
]
