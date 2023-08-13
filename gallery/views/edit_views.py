from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic.edit import CreateView


from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm


@require_http_methods(["GET", "POST"])
@permission_required("gallery.add_room", raise_exception=True)
@login_required
def add_room(request):
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

    template_name = "gallery/room_create_form.html"

    if request.method == "POST":
        # Validate submitted form

        # Populate the form with the request.POST data
        form = CreateRoomForm(request.POST, request.FILES)

        if form.is_valid():
            # Create new room
            room = Room.objects.create(
                name=form.cleaned_data["name"],
                owner=request.user,
                discription=form.cleaned_data["discription"],
            )
            # Add the background as post step
            if request.FILES:
                room.background = request.FILES["background"]

            # Save the room instance
            room.save()

            # Redirect to the room just created page
            messages.add_message(request, messages.SUCCESS, "تم إنشاء الغرفه بنجاح")
            return redirect(room.get_absolute_url())
        else:
            # Render the template with error messages
            return render(request, template_name, {"form": form})

    else:
        # Display the form for Get requests

        # Estantiate an empty form
        form = CreateRoomForm()

        # Render the template with form context variable
        return render(request, template_name, {"form": form})


@require_http_methods(["POST"])
@login_required
@permission_required("gallery.delete_room", raise_exception=True)
def delete_room(request, room_pk):
    """
    delete_room is a function based view for
    deleting an entire room including all the pictures it contain

    http_methods:
        accessible only via POST request

    login_required:
        True

    permissions:
        only users with the delete_room permission can access this function
        usually designers and superusers,

    url params:
        -room_pk:
            The room primary key
    """
    # Get room or raise not found error
    room = get_object_or_404(Room, pk=room_pk)

    # Only the owner of the room can delete it
    if room.owner == request.user:
        # Delete all the picture first
        for picture in room.pictures.all():
            picture.image.delete()

        # Get the room name
        room_name = room.name

        # Delete the room
        room.delete()

        # Redirect to user profile page
        messages.add_message(
            request, messages.SUCCESS, f'"{room_name}" deleted successfully'
        )
        return redirect(reverse("profile", args=[request.user.username]))

    else:
        return HttpResponse("premessionDenied", status=403)


@require_http_methods(["POST"])
@login_required
@permission_required("gallery.add_picture", raise_exception=True)
def add_picture_to_room(request, room_pk):
    """
    View for adding pictures into room

    http_methods:
        accessible only via POST:

    login_required:
        True

    permissions:
        only users with the add_picture permission can access this function
        usually designers and superusers,

    params:
      -room_pk: the room primary key passed via url
    """
    room = get_object_or_404(Room, pk=room_pk)

    # Process submitted request
    form = AddPictureForm(request.POST, request.FILES)
    if form.is_valid():
        # add picture into room

        # Create a new_picture instance
        new_picture = Picture.objects.create(
            image=request.FILES["image"],
            room=room,
        )

        # Save the instance
        new_picture.save()

        messages.add_message(
            request, messages.SUCCESS, "picture was added successfully"
        )

        # redirect to the room page
        return redirect(room.get_absolute_url())
    else:
        messages.add_message(request, messages.ERROR, "Couldn't add the picture")
        return redirect(room.get_absolute_url())


@require_http_methods(["POST"])
@login_required
@permission_required("gallery.delete_picture", raise_exception=True)
def delete_picture(request, picture_pk):
    """
    Function based view for deleting pictures
    from rooms

    http_methods:
        accessible via POST request

    login_required:
        True

    permissions:
        only users with the delete_picture permission can access this function
        usually designers and superusers,

    URL params :
        -picture_pk:
            The picture primary key

    """
    # get the picture object
    picture = get_object_or_404(Picture, pk=picture_pk)

    # Only the owner of room can delete pictures
    if picture.room.owner == request.user:
        # Get the room to be redirect after deleting
        redirect_room = picture.room

        # Delete the image from the filesystem
        picture.image.delete()

        # Delete the picture instance
        picture.delete()

        # Redirect to the picture room
        messages.add_message(request, messages.SUCCESS, "Picture deleted successfully")
        return redirect(redirect_room.get_absolute_url())

    else:
        # Raise a premessionDenied error
        return HttpResponse("PremessionDenied", status=403)
