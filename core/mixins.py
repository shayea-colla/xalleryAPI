from .debug import debug


class SetOwnerTheCurrentUserMixin:
    def create(self, validated_data):
        """Assume the object has owner field"""
        user = self.context["request"].user
        validated_data["owner"] = user
        return super().create(validated_data)
