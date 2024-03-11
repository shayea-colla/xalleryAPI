from time import sleep

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwnerOrReceiver


class HomePageOrder(TemplateView):
    template_name = "order/home.html"


class OrderViewSet(viewsets.ModelViewSet):
    """
    TODO
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReceiver]

    @method_decorator(csrf_protect)
    def list(self, request):
        """
        List orders where the reciver is the user requesting the orders
        except if type param was provided with 'my_orders' value, than return
        orders where orderer is the user requesting the orders
        """

        if (
            "type" in request.query_params
            and request.query_params["type"] == "my_orders"
        ):
            queryset = request.user.my_orders.all()
        else:
            queryset = request.user.orders.all()

        serializer = OrderSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        """
        Set the orderer to the user requesting to create the order
        and compare it to the receiver so they can not be equal
        """

        # Get the serializer class defined above
        serializer_class = self.get_serializer_class()

        # serialize the data
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Set the orderer to the current user, no matter what provided in the request data
            serializer.validated_data["orderer"] = request.user

            # Set the state to None in case it was provided by the request
            serializer.validated_data["state"] = None

            # Validate that both orderer (request.user) and reciever are not equal
            if (
                serializer.validated_data["orderer"]
                == serializer.validated_data["receiver"]
            ):
                return Response(
                    {"detail": "you can not order yourself"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return Bad request response with erorrs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Only receiver of the order is allowed to update the state
        """
        # Artificially delay the response three seconds
        sleep(1)

        order = get_object_or_404(self.get_queryset(), pk=kwargs["pk"])
        if request.user == order.receiver:
            return super().update(request, *args, **kwargs)

        return Response(
            {"detail": "you do not have permission to perform this action"},
            status=status.HTTP_403_FORBIDDEN,
        )

    def destroy(self, request, *args, **kwargs):
        """
        Only the orderer is allowed to delete order
        """

        order = get_object_or_404(self.get_queryset(), pk=kwargs["pk"])
        if order.orderer == request.user:
            return super().destroy(request, *args, **kwargs)

        return Response(
            {"detail": " you do not have permission to perform this action"},
            status=status.HTTP_403_FORBIDDEN,
        )
