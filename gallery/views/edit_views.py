from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic.edit import CreateView


from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm


@require_http_methods(["GET", "POST"])
@login_required
def create_room(request):
    """
    view for creating a new room
    """

    template_name = "gallery/room_create_form.html"

    if request.method == "POST":
        # Validate submitted form

        # Populate the form with the request.POST data
        form = CreateRoomForm(request.POST)

        if form.is_valid():
            # Create new room
            room = Room.objects.create(
                name=form.cleaned_data["name"],
                owner=request.user,
                discription=form.cleaned_data["discription"],
            )
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


@require_http_methods(["GET", "POST"])
@login_required
def add_picture_to_room(request, room_pk):
    """
    View for adding pictures into room

    params:
      -room_pk: the room primary key passed via url
    """
    template_name = "gallery/add_picture_form.html"
    room = get_object_or_404(Room, pk=room_pk)

    if request.method == "POST":
        # Process submitted request
        form = AddPictureForm(request.POST, request.FILES)
        print("#" * 100)
        print(form.is_valid())

        if form.is_valid():
            # add picture into room

            # Create a new_picture instance
            new_picture = Picture.objects.create(
                image=request.FILES["image"],
                room=room,
            )

            # Save the instance
            new_picture.save()

            # redirect to the room page
            messages.add_message(
                request, messages.SUCCESS, "picture was added successfully"
            )
            return redirect(room.get_absolute_url())
        else:
            messages.add_message(request, messages.ERROR, "Couldn't add the picture")
            return render(request, template_name, {"form": form})
    else:
        # Populate empty form for other request
        add_picture_form = AddPictureForm()

        context = {
            "form": add_picture_form,
            "room": room,
        }
        return render(request, template_name, context)


@require_http_methods(["POST"])
@login_required
def delete_picture(request, picture_pk):
    """
    Function based view for deleting pictures
    from rooms

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


@require_http_methods(["POST"])
@login_required
def delete_room(request, room_pk):
    """
    delete_room is a function based view for
    deleting an entire room including all the pictures it contain

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
