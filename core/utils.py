import os
from django.contrib.auth.models import Group


def is_designer(user) -> bool:
    designer_group = Group.objects.get(name="designers")
    return designer_group in user.groups.all()


def get_test_image_path():
    current_dir = os.getcwd()
    path = "/static/test_image/image.jpg"
    return os.path.join(current_dir, path)
