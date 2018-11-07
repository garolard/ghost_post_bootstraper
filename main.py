import argparse
import os
import time
import datetime
import logging
import locale

from shutil import copyfile


# Hacer esto es una mala idea aparentemente
# porque locale es global y podria joder otras
# partes del a aplicacion... Como esto es una
# herramienta personal me la pela
locale.setlocale(locale.LC_ALL, locale='Spanish')


def info(msg):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + ' INFO: ' + msg)


# root path no viene vacio porque tiene valor por defecto
# en el parser de argumentos
def build_absolute_path(path, root):
    if not path:
        raise Exception('Path cannot be empty')

    if (os.path.isdir(root + path)):
        raise Exception(root + path + ' directory already exists')

    return root + path


def create_work_dir_in_path(path):
    os.mkdir(path)
    info('Post directory created')


def create_images_dirs(path):
    if os.path.isdir(path + '/images_input'):
        raise Exception('images input dir already exists')
    if os.path.isdir(path + '/images_output'):
        raise Exception('images output dir already exists')

    for p in [path + '/images_input', path + '/images_output']:
        os.mkdir(p)

    info('Images dirs created')


def copy_post_template(path):
    if not os.path.exists(os.getcwd() + '/template.md'):
        raise Exception(
            'Post template file does not exists. A template.md file is required')

    if os.path.isfile(path + '/template.md'):
        raise Exception('The post destination file already exists')

    copyfile(os.getcwd() + '/template.md', path + '/template.md')

    info('Post template copied')


def copy_scripts(path):
    if not os.path.exists(os.getcwd() + '/scripts/process.py'):
        raise Exception('Post process script does not exists')

    copyfile(os.getcwd() + '/scripts/process.py', path + '/process.py')
    info('Post process script copied')


def init(path, rootPath):
    info('Starting bootstraper')

    try:
        absolute_path = build_absolute_path(path, rootPath)
        create_work_dir_in_path(absolute_path)
        create_images_dirs(absolute_path)
        copy_post_template(absolute_path)
        copy_scripts(absolute_path)
    except Exception as e:
        logging.exception(e)
    finally:
        info('Finishing bootstraper')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        metavar='path',
                        help='path in which the project will be created')
    parser.add_argument('--root',
                        help='absolute root path for the project',
                        default='d:/WS/', dest='rootPath')

    args = parser.parse_args()

    init(args.path, args.rootPath)
