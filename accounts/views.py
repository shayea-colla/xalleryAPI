from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic.edit import CreateView

from accounts.forms import CreateUserForm
from accounts.models import User


# Create your views here.
@require_http_methods(["GET"])
def profile(request, username):
    # Get the user or raise 404 if not found
    user = get_object_or_404(User, username=username)

    context = {"user": user}
    return render(request, "registration/profile.html", context)


@require_http_methods(["GET", "POST"])
def create_user(request):
    """
    view for creating new users
    """

    template_name = "registration/create_user_form.html"

    if request.method == "POST":
        # Bound the form data
        form = CreateUserForm(request.POST)

        # Validate data
        if form.is_valid():
            # create new user
            new_user = User.objects.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                discription=form.cleaned_data["discription"],
                password=form.cleaned_data["password"],
            )

            # redirect to the new user profile
            return redirect(reverse("profile", args=[new_user.username]))

        else:
            # render the same template with error message
            context = {
                "form": form,
            }
            return render(request, template_name, context)

    else:
        # Estantiate an empty form
        form = CreateUserForm()
        context = {
            "form": form,
        }
        return render(request, template_name, context)


# class CreateUserView(CreateView):
#    model = User
#    template_name = 'registration/create_user_form.html'
#
#    fields = ['first_name', 'last_name', 'username', 'email', 'password']

# Redirect to the login page after creating new user
#    success_url = reverse('login')

# @require_http_methods(['GET', 'POST'])
# def create_new_account(request):
#    if request.method == "POST":
#        form = CreateUserForm(request.POST)
#        if form.is_valid():
#
#            User.objects.create_user(
#                    first_name=form.cleaned_data['first_name'],
#                    last_name=form.cleaned_data['last_name'],
#                    username=form.cleaned_data['username'],
#                    password=form.cleaned_data['password'],
#                    email=form.cleaned_data['email'],
#                    discription=form.cleaned_data['discription']
#                  )
#            return redirect(reverse('login'))
#        else :
#            return render(request, 'registration/create_new_account_form.html', {
#                    'form': form,
#                })
#
#
#
#    elif request.method == "GET":
#        form = CreateUserForm()
#        return render(request, 'registration/create_new_account_form.html', {
#                'form': form,
#            })
#
