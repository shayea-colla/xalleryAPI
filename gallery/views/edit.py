from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView

from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm


# @require_http_methods(['POST', 'GET'])
# @login_required()
# @permission_required('gallery.edit_room')
# def edit_room(request, room_pk):
#
#    # Template used to update room is the same template used to create room
#    template_name = 'gallery/room_edit_form.html'
#
#    # Get the room instant or raise not found error
#    room = get_object_or_404(Room, pk=room_pk)
#
#    if request.method == 'POST':
#        if room.owner == request.user:
#            update_form = CreateRoomForm(request.POST)
#            if update_form.is_valid():
#                # update room values
#                room.name = update_form.cleaned_data['name']
#                room.discription = update_form.cleaned_data['discription']
#
#                # Save room instant
#                room.save()
#
#                # Redirect to the room page
#                return redirect(reverse('detail-room', args=[room.pk]))
#            else:
#                context = {
#                    'form': update_form,
#                    'room': room,
#                }
#                return render(
#                        request,
#                        template_name,
#                        context,
#                        status=400
#                )
#
#        else:
#            return HttpResponse('Forbidden', status=403)
#    else:
#        data = {
#            'name': room.name,
#            'discription': room.discription,
#        }
#
#        update_form = CreateRoomForm(data)
#        context = {
#                'form': update_form,
#                'room': room,
#        }
#        return render(request, template_name, context)


class UpdateRoom(LoginRequiredMixin, UpdateView):
    model = Room

    form_class = CreateRoomForm

    template_name = "gallery/room_edit_form.html"


#    def test_func(self):
#        return self.request.user == self.object.owner
