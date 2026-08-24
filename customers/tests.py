from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Customer


class CustomerAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
            is_staff=True
        )

        self.client.force_authenticate(user=self.user)

        self.customer = Customer.objects.create(
            name="Existing Customer",
            email="existing@example.com",
            phone="03001111111",
            city="Multan"
        )

    # GET
    def test_get_customers(self):
        response = self.client.get("/customers/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # POST
    def test_create_customer(self):
        data = {
            "name": "Test Customer",
            "email": "test@example.com",
            "phone": "03001234567",
            "city": "Multan"
        }

        response = self.client.post("/customers/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    # GET single customer
    def test_get_customer_detail(self):
        response = self.client.get(
            f"/customers/{self.customer.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # PUT
    def test_update_customer(self):
        data = {
            "name": "Updated Customer",
            "email": "updated@example.com",
            "phone": "03009999999",
            "city": "Lahore"
        }

        response = self.client.put(
            f"/customers/{self.customer.id}/",
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # PATCH
    def test_patch_customer(self):
        data = {
            "city": "Lahore"
        }

        response = self.client.patch(
            f"/customers/{self.customer.id}/",
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # DELETE
    def test_delete_customer(self):
        response = self.client.delete(
            f"/customers/{self.customer.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    # Validation
    def test_invalid_email(self):
        data = {
            "name": "Invalid Customer",
            "email": "wrong-email",
            "phone": "03001234567",
            "city": "Multan"
        }

        response = self.client.post(
            "/customers/",
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # Not found
    def test_customer_not_found(self):
        response = self.client.get(
            "/customers/999999/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # Filtering
    def test_filter_by_city(self):
        response = self.client.get(
            "/customers/?city=Multan"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # Searching
    def test_search_customer(self):
        response = self.client.get(
            "/customers/?search=Existing"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )