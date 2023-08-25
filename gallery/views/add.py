from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic.edit import CreateView


from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm


class CreateRoomView(
    SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    """
    view for creating a new room

    http_methods:
        accessible via GET and POST methods

    login_required:
        True

    permissions:
        only users with the add_room permission can access this function
        usually designers and superusers
    """

    permission_required = "gallery.add_room"

    template_name = "gallery/room_create_form.html"

    form_class = CreateRoomForm

    success_message = '"%(name)s" was created successfully.'

    model = Room

    def form_valid(self, form):
        # Assign the owner of the room to the requested user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AddPictureView(
    SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    """
    View for adding pictures into room

    http_methods:
        accessible only via POST:

    login_required:
        True

    permissions:
        only users with the add_picture permission can access this function
        usually designers and superusers,
    """

    permission_required = "gallery.add_picture"

    form_class = AddPictureForm

    success_message = "Picture added successfully."

    model = Picture

    def form_valid(self, form):
        """
        Validate that only owners of rooms can add pictures to it
        """

        if form.cleaned_data["room"].owner == self.request.user:
            form.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        return the room absolute url
        """

        return self.object.room.get_absolute_url()


# @require_http_methods(["GET", "POST"])
# @login_required
# @permission_required("gallery.add_room", raise_exception=True)
# def add_room(request):
#    """
#    view for creating a new room
#
#    http_methods:
#        accessible via GET and POST methods
#
#    login_required:
#        True
#
#    permissions:
#        only users with the add_room permission can access this function
#        usually designers and superusers
#    """
#
#    template_name = "gallery/room_create_form.html"
#
#    if request.method == "POST":
#        # Validate submitted form
#
#        # Populate the form with the request.POST data
#        form = CreateRoomForm(request.POST, request.FILES)
#
#        if form.is_valid():
#            # Create new room
#            room = Room.objects.create(
#                name=form.cleaned_data["name"],
#                owner=request.user,
#                discription=form.cleaned_data["discription"],
#            )
#            # Add the background as post step
#            if request.FILES:
#                room.background = request.FILES["background"]
#
#            # Save the room instance
#            room.save()
#
#            # Redirect to the room just created page
#            messages.add_message(request, messages.SUCCESS, "تم إنشاء الغرفه بنجاح")
#            return redirect(room.get_absolute_url())
#        else:
#            # Render the template with error messages
#            return render(request, template_name, {"form": form}, status=400)
#
#    else:
#        # Display the form for Get requests
#
#        # Estantiate an empty form
#        form = CreateRoomForm()
#
#        # Render the template with form context variable
#        return render(request, template_name, {"form": form})
#


# @require_http_methods(["POST"])
# @login_required
# @permission_required("gallery.add_picture", raise_exception=True)
# def add_picture_to_room(request, room_pk):
#    """
#    View for adding pictures into room
#
#    http_methods:
#        accessible only via POST:
#
#    login_required:
#        True
#
#    permissions:
#        only users with the add_picture permission can access this function
#        usually designers and superusers,
#
#    params:
#      -room_pk: the room primary key passed via url
#    """
#    room = get_object_or_404(Room, pk=room_pk)
#
#    # Process submitted request
#    form = AddPictureForm(request.POST, request.FILES)
#    if form.is_valid():
#        # add picture into room
#
#        # Create a new_picture instance
#        new_picture = Picture.objects.create(
#            image=request.FILES["image"],
#            room=room,
#        )
#
#        # Save the instance
#        new_picture.save()
#
#        messages.add_message(
#            request, messages.SUCCESS, "picture was added successfully"
#        )
#
#        # redirect to the room page
#        return redirect(room.get_absolute_url())
#    else:
#        messages.add_message(request, messages.ERROR, "Couldn't add the picture")
#        return redirect(room.get_absolute_url())
