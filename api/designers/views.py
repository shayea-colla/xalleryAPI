from django.contrib.auth.models import Group

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import User
from .serializers import UserSerializer


class ListDesignersView(ListAPIView):
    queryset = User.objects.filter(groups=Group.objects.get(name="designers"))
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class RetrieveDesignerView(RetrieveAPIView):
    queryset = User.objects.filter(groups=Group.objects.get(name="designers"))
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
