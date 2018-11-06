import argparse
import os
import time
import datetime
import logging

from shutil import copyfile


def info(msg):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + ' INFO: ' + msg)


def build_absolute_path(path, root='d:/WS/'):
    if not path:
        raise Exception('La ruta no puede estar en blanco')

    if (os.path.isdir(root + path)):
        raise Exception('El directorio ' + root + path + ' ya existe')

    return root + path


def create_work_dir_in_path(path):
    os.mkdir(path)
    info('Creado directorio de post')


def create_images_dirs(path):
    if os.path.isdir(path + '/images_input'):
        raise Exception('El directorio de entrada de imágenes ya existe')
    if os.path.isdir(path + '/images_output'):
        raise Exception('El directorio de salida de imágenes ya existe')
    
    for p in [path + '/images_input', path + '/images_output']:
        os.mkdir(p)
    
    info('Creados directorios de imágenes')


def copy_post_template(path):
    if not os.path.exists(os.getcwd() + '/template.md'):
        raise Exception('El archivo plantilla de post no existe. Se requiere un archivo \'template.md\' para usar como plantilla')

    if os.path.isfile(path + '/template.md'):
        raise Exception('El archivo de post ya existe')

    copyfile(os.getcwd() + '/template.md', path + '/template.md')
    info('Copiado archivo de plantilla de post')


def copy_scripts(path):
    if not os.path.exists(os.getcwd() + '/scripts/process.py'):
        raise Exception('No existe o no se encuentra el script de procesado de proyecto.')
    
    copyfile(os.getcwd() + '/scripts/process.py', path + '/process.py')
    info('Copiado script de procesado de proyecto')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='path', help='La ruta donde se creará el proyecto de post')

    args = parser.parse_args()

    info('Iniciando bootstraper')

    try:
        absolute_path = build_absolute_path(args.path)
        create_work_dir_in_path(absolute_path)
        create_images_dirs(absolute_path)
        copy_post_template(absolute_path)
        copy_scripts(absolute_path)
    except Exception as e:
        logging.exception(e)
    finally:
        info('Finalizando bootstraper')
