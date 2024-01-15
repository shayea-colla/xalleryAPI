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


class EditProfileView(
    UserPassesTestMixin, LoginRequiredMixin, UpdateView, SuccessMessageMixin
):
    def test_func(self):
        # Only the owner of profile can edit it
        return self.get_object() == self.request.user

    model = User
    template_name = "registration/update_profile.html"
    fields = ["username", "first_name", "last_name", "email", "discription"]
    context_variable_name = "form"
    success_message = "Profile Updated"


class CreateUserView(CreateView, SuccessMessageMixin):
    model = User
    form_class = CreateUserForm
    template_name = "registration/create_user_form.html"
    success_message = '"%(username)s" profile created successfully'

    def form_valid(self, form):
        # Save the form first so you can have access to "new_user" object
        new_user = User.objects.create_user(form.data)
        # form.save()

        # Assigne the user to the designers group
        designersGroup = Group.objects.get(name="designers")
        new_user.groups.add(designersGroup)

        # Login the new user
        login(self.request, form.instance)

        return super().form_valid(form)
