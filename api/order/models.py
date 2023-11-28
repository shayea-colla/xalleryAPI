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
    - reciever ( user "only designer")
    - date ( dateField )
    - state ( whether order has been accepted or refused or still waiting)
    """

    orderer = ForeignKey(
        User,
        related_name="my_orders",
        on_delete=PROTECT,
    )

    reciever = ForeignKey(
        User,
        related_name="orders",
        on_delete=PROTECT,
    )
    
    # The state reflect three states :
    # None : order is still waiting to be accepted or refused.
    # True : order has been accepted by reciever.
    # False: order has been rejected by reciever.
    state = BooleanField(null=True)

    date = DateField(auto_now_add=True)



    class Meta:
        ordering = ['-date']

    def __str__():
        return f"User: {self.orderer.username} ordered User: {self.reciever.username} at {date}"


    def is_accepted(self):
        return self.state == True
    
    def is_rejected(self):
        return self.state == False
    

    def is_waiting(self):
        return self.state == None

pass


class Message(Model):
    """
    fields in this model is:
    - order ( Order id " ForeignKey ")
    - date ( dateField )
    - message ( textField (by the orderer) )
    - replay ( textField "by the reciever")
    
    """
    pass
