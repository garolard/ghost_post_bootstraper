import os
import re
import time
import datetime

from utils.ioutils import get_file_content
from os.path import join, isfile


# Lo de ir meneando esta funcion por todo
# el proyecto no me gusta nada...
def info(msg):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + ' INFO: ' + msg)


# Esto es una cutrez de escalas atomicas
# pero la alternativa es instalarse babel
# y jugar con sus funciones de formateo
# o seguir pegandome con el locale que no
# funciono. De momento me conformo con esto
# porque es simple y me cubre.
def get_month_name():
    now = datetime.datetime.now()
    months = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    return months.get(now.month)


def require_template_file():
    if not isfile(join(os.getcwd(), 'template.md')):
        raise FileNotFoundError('A template.md file is needed to process post')


def require_links_file():
    if not isfile(join(os.getcwd(), 'links.txt')):
        raise FileNotFoundError('A links.txt file is needed to process post')


def read_template():
    info("Reading post template")
    require_template_file()

    fp = os.getcwd() + '/template.md'
    with open(fp, 'r', encoding='utf8') as f:
        content = f.read()

    info("Template correctly read")

    return content


def replace_date(content):
    info("Replacing date")
    require_template_file()

    pattern = r'\{{2}(.*?)\}{2}'
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%d de ' + get_month_name() + ' de %Y')

    return re.sub(pattern, timestamp, content)


def replace_links(content):
    info("Replacing links")
    require_template_file()
    require_links_file()

    # falta leer el archivo de enlaces y reemplazar en la plantilla de post

    pattern = r'\[(.*?)\]\((.*?)\)'

    return re.sub(pattern,
                  r'<a href="\2" target="_blank" rel="nofollow">\1</a>',
                  content)


def write_post(content):
    info("Writing content into destination file")
    with open(os.getcwd() + '/post.md', 'w', encoding='utf8') as f:
        f.write(content)


def process_template():
    content = read_template()
    content = replace_date(content)
    content = replace_links(content)
    write_post(content)


if __name__ == '__main__':
    process_template()
