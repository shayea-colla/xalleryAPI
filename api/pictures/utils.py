from django.contrib.auth.models import Group


def is_designer(user) -> bool:
    designer_group = Group.objects.get(name="designers")
    return designer_group in user.groups.all()


def is_owner(user, obj) -> bool:
    return obj.owner == user
