from rest_framework.generics import ListAPIView

from ..models import User
from gallery.utils import debug


class ListAccounts(ListAPIView):
    def get_queryset(self):
        queryset = super().get_queryset()
        debug(self.request.query_params)
