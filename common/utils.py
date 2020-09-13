import uuid

from django.contrib import messages


# noinspection PyProtectedMember
def get_upload_path(instance, file_name):
    """
    Takes filename and creates new one with random string at the end
    :param instance: DO NOT delete this parameter, it's required for upload_to
    :param file_name: raw file name from admin
    :return: new file name
    """
    if instance.offer is None:
        file_name, extension = file_name.split('.')
        return f'{file_name}_{str(uuid.uuid4())[:8]}.{extension}'

    model = instance.offer.__class__._meta
    model_name = model.verbose_name_plural.replace(' ', '_')
    file_name, extension = file_name.split('.')
    file_path = f'{model_name}/{file_name}_{str(uuid.uuid4())[:8]}.{extension}'
    return file_path


def message_info(request, message):
    messages.add_message(request, messages.INFO, message)


def message_error(request, message):
    messages.add_message(request, messages.ERROR, message)
