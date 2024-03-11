import os
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.profiles import NormalUser, Designer
from api.pictures.views import LikePictureAPIView, UnLikePictureAPIView

from gallery.models import Picture, Room


class TestLikePictureAPIView(TestCase):

    def setUp(self):
        """Create a few designers and nromal users"""

        self.designer = Designer.objects.create_user(
            username="test_designer",
            password="no way home",
            discription="test designer",
        )

        self.normal = NormalUser.objects.create_user(
            username="test_normal",
            password="no way home",
            discription="test normal",
        )

        self.test_room = Room.objects.create(
            name="test_room", discription="test discription", owner=self.designer
        )

        current_dir = os.getcwd()
        image_path = "static/test_image/image.jpg"
        path = os.path.join(current_dir, image_path)

        # Add the background field
        self.test_image = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(path, "rb").read(),
            content_type="image/jpg",
        )
        self.test_room.background = self.test_image
        self.test_room.save()

        self.test_picture = Picture.objects.create(
            room=self.test_room, owner=self.test_room.owner, image=self.test_image
        )

        self.factory = APIRequestFactory()
        self.view = LikePictureAPIView()
        self.client = APIClient()

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""
        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, IsAuthenticated)

    def test_view_reject_unauthorized_users(self):
        response = self.client.patch(
            reverse("like-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_does_not_accept_get_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.get(reverse("like-picture", args=[self.test_picture.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_post_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.post(
            reverse("like-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.put(reverse("like-picture", args=[self.test_picture.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.delete(
            reverse("like-picture", args=[self.test_picture.id])
        )
        self.assertTrue(response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_add_like_to_picture(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.patch(
            reverse("like-picture", args=[self.test_picture.id])
        )
        self.assertEqual(self.test_picture.likes.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


class TestUnLikePictureAPIView(TestCase):

    def setUp(self):
        """Create a few designers and nromal users"""

        self.designer = Designer.objects.create_user(
            username="test_designer",
            password="no way home",
            discription="test designer",
        )

        self.normal = NormalUser.objects.create_user(
            username="test_normal",
            password="no way home",
            discription="test normal",
        )

        self.test_room = Room.objects.create(
            name="test_room", discription="test discription", owner=self.designer
        )

        current_dir = os.getcwd()
        image_path = "static/test_image/image.jpg"
        path = os.path.join(current_dir, image_path)

        # Add the background field
        self.test_image = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(path, "rb").read(),
            content_type="image/jpg",
        )
        self.test_room.background = self.test_image
        self.test_room.save()

        self.test_picture = Picture.objects.create(
            room=self.test_room, owner=self.test_room.owner, image=self.test_image
        )

        self.factory = APIRequestFactory()
        self.view = UnLikePictureAPIView()
        self.client = APIClient()

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""
        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, IsAuthenticated)

    def test_view_reject_unauthorized_users(self):
        response = self.client.get(
            reverse("unlike-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_does_not_accept_get_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.get(
            reverse("unlike-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_post_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.post(
            reverse("unlike-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.put(
            reverse("unlike-picture", args=[self.test_picture.id])
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.delete(
            reverse("unlike-picture", args=[self.test_picture.id])
        )
        self.assertTrue(response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_like_than_unlike_picture(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.patch(
            reverse("like-picture", args=[self.test_picture.id])
        )
        self.assertEqual(self.test_picture.likes.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        response = self.client.patch(
            reverse("unlike-picture", args=[self.test_picture.id])
        )

        self.assertEqual(self.test_picture.likes.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


#     def test_getting_only_designers_when_no_type_specified(self):
#         client = APIClient()
#         response = client.get("/api/accounts/")
#         # Assert there is 20 results ( only designers )
#         self.assertEqual(len(response.data), self.num_designers)

#         for user in response.data:
#             self.assertEqual(user["type"], "DESIGNER")

#     def test_getting_only_normal_user_when_type_is_normal(self):
#         client = APIClient()
#         response = client.get("/api/accounts/?type=normal")
#         # Assert there is 20 results ( only normal )
#         self.assertEqual(len(response.data), self.num_normal_users)

#         for user in response.data:
#             self.assertEqual(user["type"], "NORMAL")

#     def test_view_uses_designer_serializer_when_no_type_specified(self):
#         client = APIClient()
#         response = client.get("/api/accounts/")

#         # Assert there is 20 results ( only designers )
#         self.assertEqual(len(response.data), self.num_designers)

#         for user in response.data:
#             self.assertTrue("designermore" in user)

#     def test_view_status_code_is_201_when_create_normal_user(self):
#         client = APIClient()
#         data = {
#             "username": "new_test_user",
#             "password": "no way home",
#             "discription": "new_test_user discription",
#         }
#         response = client.post("/api/accounts/?type=normal", data=data, format="json")

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_view_create_normal_user_when_valid_post_request(self):
#         client = APIClient()
#         data = {
#             "username": "new_test_user",
#             "password": "no way home",
#             "discription": "new_test_user discription",
#         }
#         response = client.post("/api/accounts/?type=normal", data=data, format="json")

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data.get("type"), "NORMAL")

#     def test_view_create_designer_when_valid_post_request(self):
#         client = APIClient()
#         data = {
#             "username": "new_test_user",
#             "password": "no way home",
#             "discription": "new_test_user discription",
#             "designermore": {
#                 "favorate_application": "Vim",
#             },
#         }

#         response = client.post("/api/accounts/", data=data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data.get("type"), "DESIGNER")

#     """There is an error with this wsgi request, it doesn't have a `query_params` attribute , causing error on the test"""

#     def test_view_returns_correct_serializer_class_with_request_factory(self):
#         request = self.factory.get(
#             "/api/accounts/?type=designer",
#             query_params={"type": "designer"},
#             format="json",
#         )

#         view = ListCreateAccountsAPIView()
#         view.dispatch(request)

#         serializer_class = view.get_serializer_class()

#         self.assertEqual(serializer_class, DesignerSerializer)

#     def test_view_returns_correct_designer_queryset_with_request_factory(self):
#         request = self.factory.get(
#             "/api/accounts/?type=designer",
#             query_params={"type": "designer"},
#             format="json",
#         )

#         view = ListCreateAccountsAPIView()
#         view.dispatch(request)

#         queryset = view.get_queryset()

#         for user in queryset:
#             self.assertEqual(user.type, "DESIGNER")

#     def test_view_returns_correct_normal_user_queryset_with_request_factory(self):
#         request = self.factory.get(
#             "/api/accounts/?type=normal",
#             query_params={"type": "designer"},
#             format="json",
#         )

#         view = ListCreateAccountsAPIView()
#         view.dispatch(request)

#         queryset = view.get_queryset()

#         for user in queryset:
#             self.assertEqual(user.type, "NORMAL")


# class TestRetrieveUpdateDestroyAccountAPIView(TestCase):
#     num_designers = 10
#     num_normal_users = 5

#     @classmethod
#     def setUpTestData(self):
#         """Create a few designers and nromal users"""

#         for i in range(self.num_designers):
#             Designer.objects.create_user(
#                 username=f"test_designer{i}",
#                 password=f"no way home",
#                 discription=f"test designer",
#             )

#         for i in range(self.num_normal_users):
#             NormalUser.objects.create_user(
#                 username=f"test_normal{i}",
#                 password=f"no way home",
#                 discription=f"test normal",
#             )

#         self.factory = APIRequestFactory()

#     def test_permission_classes(self):
#         """Test permission classess is AllowAny"""
#         view = RetrieveUpdateDestroyAccountAPIView()
#         self.assertEqual(len(view.permission_classes), 1)
#         permission_class = view.permission_classes[0]
#         self.assertEqual(permission_class, IsAccountOwnerOrReadOnly)

#     def test_view_accept_get_request(self):
#         client = APIClient()
#         response = client.get("/api/accounts/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_view_do_not_accept_post_request(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.post(f"/api/accounts/{test_user.id}/")

#         self.assertTrue(response.status_code == HTTP_405_METHOD_NOT_ALLOWED)

#     def test_view_accept_patch_request(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.patch(f"/api/accounts/{test_user.id}/")

#         # Assert that the response code is not `method not allowd`.
#         # It won't be 200 ok , because you didn't provide the patch data
#         self.assertTrue(response.status_code != HTTP_405_METHOD_NOT_ALLOWED)

#     def test_view_accept_put_request(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.put(f"/api/accounts/{test_user.id}/")

#         # Assert that the response code is not `method not allowd`.
#         # It won't be 200 ok , because you didn't provide the put data
#         self.assertTrue(response.status_code != HTTP_405_METHOD_NOT_ALLOWED)

#     def test_view_accept_delete_request(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.delete(f"/api/accounts/{test_user.id}/")

#         # Assert that the response code is not `method not allowd`.
#         # It won't be 200 ok , because you didn't provide valid credentials
#         self.assertTrue(response.status_code != HTTP_405_METHOD_NOT_ALLOWED)

#     def test_retrieving_specific_designer_by_id(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.get(f"/api/accounts/{test_user.id}/")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Assert we are getting the specific user
#         self.assertEqual(response.data["username"], test_user.username)
#         self.assertEqual(response.data["id"], test_user.id)

#     def test_updating_account_without_providing_valid_credentials(self):
#         client = APIClient()
#         test_user = Designer.objects.first()
#         response = client.put(f"/api/accounts/{test_user.id}/")

#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_updating_another_user_account(self):
#         client = APIClient()
#         client.login(username="test_designer1", password="no way home")
#         test_user = Designer.objects.get(username="test_designer2")

#         response = client.put(f"/api/accounts/{test_user.id}/")

#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_partial_updating_another_user_account(self):
#         client = APIClient()
#         client.login(username="test_designer1", password="no way home")
#         test_user = Designer.objects.get(username="test_designer2")

#         response = client.patch(f"/api/accounts/{test_user.id}/")

#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
