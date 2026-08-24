from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView

urlpatterns = [
    path("customers/", CustomerListCreateView.as_view()),
    path("customers/<int:customer_id>/", CustomerDetailView.as_view()),
]