from api.tags.models import Tag


def clean_tags(tags):
    """Clean a list of tags ( list of strings )"""
    # Strip white spaces
    tags = map(lambda tag: tag.strip(), tags)

    # Exclude empty strings
    tags = filter(lambda tag: tag != "", tags)

    # remove duplicate tags
    return remove_duplicate_tags(tags)


def remove_duplicate_tags(tags):
    """Remove duplicate Tags from a list by convert it to a set"""
    return set(tags)

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
        else:
            print(f"object: {obj}")

    return
