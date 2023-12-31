import uuid
from django.urls import reverse
from django.db.models import (
    Model,
    UUIDField,
    ImageField,
    CharField,
    ForeignKey,
    ManyToManyField,
    TextField,
    DateTimeField,
    BooleanField,
    PROTECT,
    CASCADE,
)

from accounts.models import User

# Create your models here.
#


class Order(Model):
    """
    fields in this model is:
    - orderer ( user foreignKey " normal or designer " )
    - receiver ( user "only designer")
    - date ( dateField )
    - state ( whether order has been accepted or refused or still waiting)
    """

    orderer = ForeignKey(
        User,
        related_name="my_orders",
        on_delete=PROTECT,
        null=False,
    )

    receiver = ForeignKey(
        User,
        related_name="orders",
        on_delete=PROTECT,
        null=False,
    )

    # The state reflect three states :
    # None : order is still waiting to be accepted or refused.
    # True : order has been accepted by receiver.
    # False: order has been rejected by receiver.
    state = BooleanField(null=True, default=None)

    message = TextField(null=False, blank=False)

    date = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"User: {self.orderer.username} ordered User: {self.receiver.username} at {self.date}"

    def get_absolute_url(self):
        return reverse("order-detail")

    def is_accepted(self):
        return self.state == True

    def is_rejected(self):
        return self.state == False

    def is_waiting(self):
        return self.state == None


class Replay(Model):
    order_id = ForeignKey(Order, on_delete=CASCADE, related_name="replies")

    message = TextField(null=False, blank=False)

    sender = ForeignKey(User, on_delete=CASCADE)

    date = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
