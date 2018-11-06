import argparse
import os
import time
import datetime


def create_work_dir_in_path(path, root='d:/WS/'):
    if not path:
        error('La ruta no puede estar en blanco')
        return

    if (os.path.isdir(root + path)):
        error('El directorio ya existe')
        return

    os.mkdir(root + path)
    info('Creado directorio de post')


def info(message):
    log(message)


def error(message):
    log(message, severity=' ERROR: ')


def log(message, severity=' INFO:  '):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + severity + message)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='path', help='La ruta donde se creará el proyecto de post')

    args = parser.parse_args()

    info('Iniciando bootstraper')
    # Esto deberia generar un error y salir del programa
    create_work_dir_in_path(args.path)

    info('Finalizando bootstraper')
