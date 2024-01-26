class SetOwnerTheCurrentUserMixin:
    def validate(self, data):
        """Assume the object has owner field"""
        user = self.context["request"].user
        data["owner"] = user
        return data
