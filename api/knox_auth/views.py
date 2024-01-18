from rest_framework.authentication import BasicAuthentication
from knox.views import LoginView as KnoxLoginView

from gallery.utils import debug


# Create your views here.
class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
