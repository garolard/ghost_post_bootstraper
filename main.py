#!/usr/bin/env python3

import os
import time
import datetime


def create_work_dir_in_path(path, root='d:/WS/'):
    if not path:
        error('La ruta no puede estar en blanco')
        return

    if (os.path.isdir(path)):
        error('El directorio ya existe')
        return

    os.mkdir(root + path)


def info(message):
    log(message)


def error(message):
    log(message, severity=' ERROR: ')


def log(message, severity=' INFO:  '):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + severity + message)


if __name__ == '__main__':
    info('Iniciando bootstraper')
    # Esto deberia generar un error y salir del programa
    create_work_dir_in_path('')

    info('Finalizando bootstraper')
