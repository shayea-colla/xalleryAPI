from .managers import DesignerManager, NormalUserManager
from .models import User


class Designer(User):
    base_type = User.Types.DESIGNER
    objects = DesignerManager()

    class Meta:
        proxy = True


class NormalUser(User):
    base_type = User.Types.NORMAL
    objects = NormalUserManager()

    class Meta:
        proxy = True

    def normal_user_method(self):
        return "I am a normal user"
