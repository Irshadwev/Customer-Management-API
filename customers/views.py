from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Customer
from .serializers import CustomerSerializer
from .permission import IsStaffOrReadOnly


class CustomerListCreateView(ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["city"]
    search_fields = ["name", "email"]


class CustomerDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsStaffOrReadOnly]

    lookup_field = "id"
    lookup_url_kwarg = "customer_id"