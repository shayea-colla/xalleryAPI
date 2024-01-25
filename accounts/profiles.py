from .managers import DesignersManager, NormalUserManager
from .models import User


class Designer(User):
    base_type = User.Types.DESIGNER
    objects = DesignersManager()

    class Meta:
        proxy = True


class NormalUser(User):
    base_type = User.Types.NORMAL
    objects = NormalUserManager()

    class Meta:
        proxy = True

    def normal_user_method(self):
        return "I am normal user"
