from rest_framework import serializers

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64' in data:
                # Break out the header from the base64 content
                header , data = data.split(';base64')

            # Try to decod the file. Return validation error if it fails
            try :
                decoded_file = base64.b64deconde(data)
            except TypeError:
                self.fail('invalid_image')


            # Generate file name:
            file_name = str(uui.uuid4())[:12]
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (filename, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

            
        return super(Base64ImageField, self).to_internal_value(data)


    def get_file_extention(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

