from rest_framework.authentication import BasicAuthentication
from knox.views import LoginView as KnoxLoginView
from accounts.api.serializers import UserSerializer

from core.debug import debug, line


# Create your views here.
class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
