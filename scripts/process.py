import os
import re
import time
import datetime


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
    if not os.path.isfile(os.getcwd() + '/template.md'):
        raise Exception('No se encuentra el archivo de plantilla de post')


def read_template():
    require_template_file()

    fp = os.getcwd() + '/template.md'
    with open(fp, 'r', encoding='utf8') as f:
        content = f.read()

    return content


def replace_date(content):
    require_template_file()

    pattern = r'\{{2}(.*?)\}{2}'
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%d de ' + get_month_name() + ' de %Y')

    return re.sub(pattern, timestamp, content)


def replace_links(content):
    require_template_file()

    pattern = r'\[(.*?)\]\((.*?)\)'

    return re.sub(pattern,
                  r'<a href="\2" target="_blank" rel="nofollow">\1</a>',
                  content)


def write_post(content):
    with open(os.getcwd() + '/post.md', 'w', encoding='utf8') as f:
        f.write(content)


def process_template():
    content = read_template()
    content = replace_date(content)
    content = replace_links(content)
    write_post(content)


if __name__ == '__main__':
    process_template()
