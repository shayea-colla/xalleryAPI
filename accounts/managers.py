from django.contrib.auth.models import UserManager
from django.db.models.query import QuerySet
from accounts.models import User


class NormalUserManager(UserManager):
    def get_queryset(self) -> QuerySet:
        results = super().get_queryset()
        return results.filter(type=User.Types.NORMAL)


class DesignerManager(UserManager):
    def get_queryset(self) -> QuerySet:
        results = super().get_queryset()
        return results.filter(type=User.Types.DESIGNER)
