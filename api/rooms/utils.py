from api.tags.models import Tag


def clean_tags(tags):
    """Clean a list of tags ( list of strings )"""
    # Strip white spaces
    tags_iter = map(lambda tag: tag.strip(), tags)
    # Exclude empty strings
    tags_filter = filter(lambda tag: tag != "", tags_iter)
    # remove duplicate tags
    return set(tags_filter)


def create_tags(tags):
    """
    Create all tags in the "tags" list
    Args:
        tags (iterable): an iterable that contains strings representing tags names
    """
    for tag in tags:
        # Use get_or_create to created only the new ones
        obj, created = Tag.objects.get_or_create(name=tag)
        if created:
            print(f"created new object: {obj}")
    return
