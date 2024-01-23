from rest_framework.serializers import ModelSerializer
from accounts.models import User
from gallery.utils import debug


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "profile_picture",
        )

    def save(self):
        """
        Use create_user method for creating new user
        because it hashes the password beofre storing
        in the database
        """
        return User.objects.create_user(self.validated_data)
