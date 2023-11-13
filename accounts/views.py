from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

# My own applications imports
from accounts.forms import CreateUserForm
from accounts.models import User


# Create your views here.
class ProfileView(DetailView):
    model = User
    context_variable_name = "user"
    template_name = "registration/profile.html"



class EditProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    def test_func(self):
        # Only the owner of profile can edit it 
        return self.get_object() == self.request.user
        

    model = User
    template_name = "registration/update_profile.html"
    fields = ['username', 'first_name', 'last_name', 'email', 'discription']
    context_variable_name = "form"
    success_message = 'Profile Updated'



class CreateUserView(CreateView, SuccessMessageMixin):
    model = User
    form_class = CreateUserForm
    template_name = "registration/create_user_form.html"
    success_message = '"%(username)s" profile created successfully'


    def form_valid(self, form):
        # Save the form first so you can have access to "new_user" object
        form.save()

        # Assigne the user to the designers group
        designersGroup = Group.objects.get(name="designers")
        form.instance.groups.add(designersGroup)

        # Login the new user
        login(self.request, form.instance)

        return super().form_valid(form)


#@require_http_methods(["GET", "POST"])
#def add_user(request):
#    """
#    view for adding new users
#    """
#
#    template_name = "registration/create_user_form.html"
#
#    if request.method == "POST":
#        # Bound the form data
#        form = CreateUserForm(request.POST)
#
#        # Validate data
#        if form.is_valid():
#            # create new user
#            new_user = User.objects.create_user(
#                first_name=form.cleaned_data["first_name"],
#                last_name=form.cleaned_data["last_name"],
#                username=form.cleaned_data["username"],
#                email=form.cleaned_data["email"],
#                discription=form.cleaned_data["discription"],
#                password=form.cleaned_data["password"],
#            )
#        
#            # Assigne the user to the designers group
#            designersGroup = Group.objects.get(name="designers")
#            new_user.groups.add(designersGroup)
#
#            # Save the user instance
#            new_user.save()
#
#            # login new_user
#            login(request, new_user)
#
#            messages.add_message(request, messages.SUCCESS, "Your account created successfully.") 
#            # redirect to the new user profile
#            return redirect(reverse("profile", args=[new_user.pk]))
#
#        else:
#            # render the same template with error message
#            context = {
#                "form": form,
#            }
#            return render(request, template_name, context)
#
#    else:
#        # Estantiate an empty form
#        form = CreateUserForm()
#        context = {
#            "form": form,
#        }
#        return render(request, template_name, context)
