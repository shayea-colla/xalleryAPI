import uuid
from django.urls import reverse
from django.db.models import (
    Model,
    UUIDField,
    ImageField,
    CharField,
    ForeignKey,
    TextField,
    DateField,
    PROTECT,
    CASCADE,
)


# Create your models here.
class Picture(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = ImageField(upload_to="pictures/")
    room = ForeignKey(
        "Room",
        related_name="pictures",
        on_delete=CASCADE,
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

    def error_message_gen(self):
        name = self.name
        error_messages = {
            "null": "This field is required",
            "unique": 'This name "{name}" is already bean used',
        }
        return error_messages

    name = CharField(
        max_length=150,
        help_text="Enter a name for the Room",
        unique=True,
        blank=False,
        #           error_messages=error_message_gen,
    )

    owner = ForeignKey("accounts.User", related_name="rooms", on_delete=PROTECT)

    background = ImageField(
        upload_to="rooms_background/",
        help_text="Set a background ( Optional )",
        null=True,
        blank=True,
    )

    discription = TextField(help_text="Describe your room ( Optional )", blank=True)

    created_at = DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("detail-room", args=[self.id])

    def __str__(self):
        return self.name
