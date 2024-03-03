import uuid
from django.urls import reverse
from django.db.models import (
    Model,
    UUIDField,
    ImageField,
    CharField,
    ForeignKey,
    ManyToManyField,
    DateField,
    CASCADE,
    PROTECT,
)

from api.tags.models import Tag


# Create your models here.
class Picture(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = ForeignKey("accounts.User", related_name="pictures", on_delete=CASCADE)
    image = ImageField(upload_to="pictures/")
    room = ForeignKey("Room", related_name="pictures", on_delete=CASCADE, null=True)
    likes = ManyToManyField(
        "accounts.User", verbose_name="Likes", related_name="liked_pictures", blank=True
    )

    def __str__(self):
        return str(self.id)


class Room(Model):
    id = UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    error_messages = {
        "null": "This field is required",
        "unique": "This name is already bean used",
    }

    name = CharField(
        max_length=150,
        help_text="Enter a name for the Room",
        unique=False,
        blank=False,
    )

    owner = ForeignKey("accounts.User", related_name="rooms", on_delete=CASCADE)

    background = ImageField(
        upload_to="rooms_background/",
        max_length=1000,
        help_text="Set a background for the room",
        blank=False,
        null=False,
    )

    #    blur_background = ImageField( upload_to="rooms_background/", help_text="Set a background",)

    discription = CharField(
        max_length=150,
        help_text="Describe your room ( maximum letters 150 )",
        blank=False,
        null=False,
    )

    created_at = DateField(auto_now_add=True)

    tags = ManyToManyField(Tag, verbose_name="Tags", related_name="rooms", blank=True)

    likes = ManyToManyField(
        "accounts.User", verbose_name="Likes", related_name="liked_rooms", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("rooms:room-detail", args=[self.id])

    def __str__(self):
        return self.name
