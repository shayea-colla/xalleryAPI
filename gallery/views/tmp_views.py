from django.views.generic.base import RedirectView


class RedirectView(RedirectView):
    parmanent = False
    query_string = True
    pattern_name = "list-all-rooms"
