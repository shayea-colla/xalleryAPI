from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import  SingleObjectMixin

from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm
from gallery.utils import debug


class CreateRoomView(
    SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    """
    __Description:
        view for creating a new room

    __Specifications:
        http_methods:
            accessible via GET and POST methods

        login_required:
            True

        permissions:
            only users with the add_room permission can access this function
            usually designers and superusers
    """

    http_method_names = ['get', 'post']
    permission_required = "gallery.add_room"

    template_name = "gallery/room_create_form.html"

    form_class = CreateRoomForm

    success_message = '"%(name)s" created successfully.'

    model = Room

    def form_valid(self, form):
        # Assign the owner of the room to the requested user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AddPictureView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView,
):
    """
    __Description: 
        View for adding pictures into room

    __Specifications:
        the view should be able to do the following:

        - process a form submitted using the AddPictureForm class
        - assign the picture with its room
        - assign the picture with the owner of the room (the one who add it)
        - add new pictures to database and filesystem
       *- redirect to the room page picture was added to it with either success of failer message
        - except only post request
        - reject unautherized users (permission requiered)
        - reject unauthenticated users (login required)

    """

    http_method_names = ['post']

    permission_required = "gallery.add_picture"

    form_class = AddPictureForm
    
    success_message = "Picture added successfully"

    model = Picture


    def form_valid(self, form):
        if form.cleaned_data['room'].owner == self.request.user:
            form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Invalid picture")
        debug(form.fields.items)



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
#   permissions:
#       only users with the add_picture permission can access this function
#       usually designers and superusers,
#
#   params:
#     -room_pk: the room primary key passed via url
#   """
#   room = get_object_or_404(Room, pk=room_pk)
#
#   # Process submitted request
#   form = AddPictureForm(request.POST, request.FILES)
#   if form.is_valid():
#       # add picture into room
#
#       # Create a new_picture instance
#       new_picture = Picture.objects.create(
#           image=request.FILES["image"],
#           room=room,
#       )
#
#       # Save the instance
#       new_picture.save()
#
#       messages.add_message(
#           request, messages.SUCCESS, "picture was added successfully"
#       )
#
#       # redirect to the room page
#       return redirect(room.get_absolute_url())
#   else:
#       messages.add_message(request, messages.ERROR, "Couldn't add the picture")
#       return redirect(room.get_absolute_url())
#

