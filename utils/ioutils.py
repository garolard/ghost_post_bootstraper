import os


def get_file_content(path):
    if not path:
        raise ValueError('Path must not be empty')
    if not os.path.isfile(path):
        raise ValueError('Path must be an existing file path')

    content = ''

    with open(path) as f:
        content = f.read()

    return content
