from django.contrib.auth.models import Group

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import User
from .serializers import DesignerSerializer, DesignerMoreSerializer
from .models import Designer, DesignerMore


class ListDesignersView(ListAPIView):
    queryset = Designer.designers.all()
    serializer_class = DesignerSerializer
    permission_classes = [AllowAny]


class RetrieveDesignerView(RetrieveAPIView):
    queryset = Designer.designers.all()
    serializer_class = DesignerSerializer
    permission_classes = [AllowAny]


class CreateDesigner(CreateAPIView):
    queryset = Designer.designers.all()
    serializer_class = DesignerSerializer
    permission_classes = [AllowAny]
