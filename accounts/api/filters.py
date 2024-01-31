from rest_framework.filters import BaseFilterBackend

from api.rooms.utils import clean_tags

from core.debug import debug


class AccountTagsFilter(BaseFilterBackend):
    """
    Temporarly FilterBackend for ListCreateAccountsAPIView.

    Note: you need to remove this filter and create General Filter that can be applied on any View
    """

    def filter_queryset(self, request, queryset, view):
        """filter queryset based on the tags url parameter

        Args:
            request : the request object used on the view that called this method
            queryset: the queyset the filter will be applied upon it
            view : the view that called this method
        """
        # Get the tags
        tags = request.query_params.get("tags")

        # Get the filter name will be used on the filter funtion
        # queyset.filter(tags_filter_field_name=tag)
        tags_field_name = getattr(view, "tags_field_name", "tags")

        if tags is not None:
            tags = clean_tags(tags.split(","))

            for tag in tags:
                queryset = queryset.filter(designermore__tags=tag)

        return queryset
