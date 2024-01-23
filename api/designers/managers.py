from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet
from accounts.models import User


class DesignersManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        results = super().get_queryset()
        return results.filter(type=User.Types.DESIGNER)
