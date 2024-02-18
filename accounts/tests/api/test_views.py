from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from accounts.api.filters import AccountTagsFilter

from accounts.api.views import ListCreateAccountsAPIView
from accounts.models import User
from accounts.profiles import NormalUser, Designer
from core.debug import debug


class TestListCreateAccount(TestCase):
    num_designers = 20
    num_normal_users = 10

    @classmethod
    def setUpTestData(self):
        """Create a few designers and nromal users"""

        for i in range(self.num_designers):
            Designer.objects.create_user(
                username=f"test_designer {i}",
                password=f"no way home",
                discription=f"test designer",
            )

        for i in range(self.num_normal_users):
            NormalUser.objects.create_user(
                username=f"test_normal {i}",
                password=f"no way home",
                discription=f"test normal",
            )

        self.factory = APIRequestFactory()

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""
        view = ListCreateAccountsAPIView()
        self.assertEqual(len(view.permission_classes), 1)
        permission_class = view.permission_classes[0]
        self.assertEqual(permission_class, AllowAny)

    def test_filter_backends(self):
        """Test filter backends contain accountTagsFilter"""
        view = ListCreateAccountsAPIView()
        filter_backends = view.filter_backends
        self.assertTrue(AccountTagsFilter in filter_backends)

    def test_view_accept_get_request(self):
        client = APIClient()
        response = client.get("/api/accounts/")
        self.assertTrue(response.status_code != HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_accept_post_request(self):
        client = APIClient()
        response = client.post("/api/accounts/")
        self.assertTrue(response.status_code != HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_patch_request(self):
        client = APIClient()
        response = client.patch("/api/accounts/")
        self.assertTrue(response.status_code == HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        client = APIClient()
        response = client.put("/api/accounts/")
        self.assertTrue(response.status_code == HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        client = APIClient()
        response = client.delete("/api/accounts/")
        self.assertTrue(response.status_code == HTTP_405_METHOD_NOT_ALLOWED)

    def test_getting_only_designers_when_no_type_specified(self):
        client = APIClient()
        response = client.get("/api/accounts/")
        # Assert there is 20 results ( only designers )
        self.assertEqual(len(response.data), self.num_designers)

        for user in response.data:
            self.assertEqual(user["type"], "DESIGNER")

    def test_getting_only_normal_user_when_type_is_normal(self):
        client = APIClient()
        response = client.get("/api/accounts/?type=normal")
        # Assert there is 20 results ( only normal )
        self.assertEqual(len(response.data), self.num_normal_users)

        for user in response.data:
            self.assertEqual(user["type"], "NORMAL")

    def test_view_uses_designer_serializer_when_no_type_specified(self):
        client = APIClient()
        response = client.get("/api/accounts/")

        # Assert there is 20 results ( only designers )
        self.assertEqual(len(response.data), self.num_designers)

        for user in response.data:
            self.assertTrue("designermore" in user)

    def test_view_status_code_is_201_when_create_normal_user(self):
        client = APIClient()
        data = {
            "username": "new_test_user",
            "password": "no way home",
            "discription": "new_test_user discription",
        }
        response = client.post("/api/accounts/?type=normal", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_create_normal_user_when_valid_post_request(self):
        client = APIClient()
        data = {
            "username": "new_test_user",
            "password": "no way home",
            "discription": "new_test_user discription",
        }
        response = client.post("/api/accounts/?type=normal", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("type"), "NORMAL")

    def test_view_create_designer_when_valid_post_request(self):
        client = APIClient()
        data = {
            "username": "new_test_user",
            "password": "no way home",
            "discription": "new_test_user discription",
            "designermore": {
                "favorate_application": "Vim",
            },
        }

        response = client.post("/api/accounts/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("type"), "DESIGNER")

    """There is an error with this wsgi request, it doesn't have a `query_params` attribute , causing error on the test"""


#    def test_view_returns_correct_serializer_class_with_request_factory(self):
#        request = self.factory.get(
#            "/api/accounts/?type=designer",
#            query_params={"type": "designer"},
#            format="json",
#        )
#        view = ListCreateAccountsAPIView()
#        view.setup(request)
#
#        serializer_class = view.get_serializer_class()
#        expected_serializer_class = DesignerSerializer()
#
#        self.assertEqual(serializer_class, expected_serializer_class)


class TestRetrieveUpdateDestroyAccountAPIView(TestCase):
    pass
