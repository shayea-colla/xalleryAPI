from .debug import debug, line


class SetOwnerTheCurrentUserMixin:
    """
    set the owner of the object to the current user
    """

    def create(self, validated_data):
        """Assume the object has owner field"""
        user = self.context.get("request").user
        validated_data = validated_data.copy()
        validated_data["owner"] = user
        return validated_data
