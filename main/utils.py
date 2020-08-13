import uuid


def get_file_name(instance, filename):
    """
    Takes filename and creates new one with random string at the end
    :param instance: DO NOT delete this parameter, it's required for upload_to
    :param filename: raw file name from admin
    :return: new file name
    """
    name, extension = filename.split('.')
    filename = f'{name}_{str(uuid.uuid4())[:8]}.{extension}'
    return filename
