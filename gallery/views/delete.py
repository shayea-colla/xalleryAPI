from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import DeleteView 
from django.views.generic.base import View
from django.views.generic.edit import ProcessFormView
from django.views.generic.detail import SingleObjectMixin

from django.views.decorators.http import require_http_methods 

from gallery.models import Picture, Room

class DeleteRoomView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    __Description:

    __Specifications:
        -
        -
        -
        -
        -
        -
    """
    http_method_names = ['post']
    model = Room

    def test_func(self):
        # Only the owner of the room can delete it
        self.object = self.get_object()
        return True #self.get_object().owner == self.request.user

    def get_success_url(self, *args, **kwargs):
        return self.request.user.get_absolute_url()

    def post(self, request, *args, **kwargs):

        # For readability 
        room = self.object
        
        # Delete all the picture first
        for picture in room.pictures.all():
            picture.image.delete()
        
        # Get the room name
        room_name = room.name
        
        # Delete the room
        room.background.delete()
        room.delete()
        
        # Redirect to user profile page
        messages.add_message(
            request, messages.SUCCESS, f'"{room_name}" deleted successfully'
        )
        return redirect(self.get_success_url())




class DeletePictureView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    __Description:

    __Specifications:
        -
        -
        -
        -
        -
        -
    """
    http_method_names = ['post']
    model = Picture

    def get_success_url(self):
        return self.redirect_path

    def test_func(self):
        # Only the owner of the room can delete it
        # Assign the object attribute manually 
        self.object = self.get_object()
        self.redirect_path = self.object.room.get_absolute_url()

        return self.object.room.owner == self.request.user



#@require_http_methods(["POST"])
#@login_required
#@permission_required("gallery.delete_picture", raise_exception=True)
#def delete_picture(request, picture_pk):
#    """
#    Function based view for deleting pictures
#    from rooms
#
#    http_methods:
#        accessible via POST request
#
#    login_required:
#        True
#
#    permissions:
#        only users with the delete_picture permission can access this function
#        usually designers and superusers,
#
#    URL params :
#        -picture_pk:
#            The picture primary key
#
#    """
#    # get the picture object
#    picture = get_object_or_404(Picture, pk=picture_pk)
#
#    # Only the owner of room can delete pictures
#    if picture.room.owner == request.user:
#        # Get the room to be redirect after deleting
#        redirect_room = picture.room
#
#        # Delete the image from the filesystem
#        picture.image.delete()
#
#        # Delete the picture instance
#        picture.delete()
#
#        # Redirect to the picture room
#        messages.add_message(request, messages.SUCCESS, "Picture deleted successfully")
#        return redirect(redirect_room.get_absolute_url())
#
#    else:
#        # Raise a premessionDenied error
#        return HttpResponse("PremessionDenied", status=403)


#@require_http_methods(["POST"])
#@login_required
#@permission_required("gallery.delete_room", raise_exception=True)
#def delete_room(request, room_pk):
#    """
#    delete_room is a function based view for
#    deleting an entire room including all the pictures it contain
#
#    http_methods:
#        accessible only via POST request
#
#    login_required:
#        True
#
#    permissions:
#        only users with the delete_room permission can access this function
#        usually designers and superusers,
#
#    url params:
#        -room_pk:
#            The room primary key
#    """
#    # Get room or raise not found error
#    room = get_object_or_404(Room, pk=room_pk)
#
#    # Only the owner of the room can delete it
#    if room.owner == request.user:
#        # Delete all the picture first
#        for picture in room.pictures.all():
#            picture.image.delete()
#
#        # Get the room name
#        room_name = room.name
#
#        # Delete the room
#        room.delete()
#
#        # Redirect to user profile page
#        messages.add_message(
#            request, messages.SUCCESS, f'"{room_name}" deleted successfully'
#        )
#        return redirect(reverse("profile", args=[request.user.pk]))
#
#    else:
#        return HttpResponse("premessionDenied", status=403)
#
def println(message):
    print()
    print("-" * 150)
    print()
    print(message)
    print()
    print("-" * 150)
    print()
