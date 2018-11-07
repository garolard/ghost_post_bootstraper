import os
import re


def process_template():
    if not os.path.isfile(os.getcwd() + '/template.md'):
        raise Exception('No se encuentra el archivo de plantilla de post')

    pattern = r'\[(.*?)\]\((.*?)\)'

    fp = os.getcwd() + '/template.md'
    with open(fp, 'r', encoding='utf8') as f:
        content = f.read()

    result = re.sub(pattern,
                    r'<a href="\2" target="_blank" rel="nofollow">\1</a>',
                    content)

    with open(os.getcwd() + '/post.md', 'w', encoding='utf8') as of:
        of.write(result)


if __name__ == '__main__':
    process_template()
