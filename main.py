import argparse
import os
import time
import datetime
import logging

from shutil import copyfile
from os.path import join, isfile
from os import listdir


def info(msg):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp + ' INFO: ' + msg)


def create_work_dir_in_path(path):
    os.mkdir(path)
    info('Post directory created')


def create_images_dirs(path):
    info('Creating image dirs')

    if os.path.isdir(path + '/images_input'):
        raise Exception('images input dir already exists')
    if os.path.isdir(path + '/images_output'):
        raise Exception('images output dir already exists')

    for p in [path + '/images_input', path + '/images_output']:
        os.mkdir(p)


def copy_post_template(path):
    info('Copying templates')

    if not os.path.exists(os.getcwd() + '/template.md'):
        raise Exception(
            'Post template file does not exists. A template.md file is required')

    if os.path.isfile(path + '/template.md'):
        raise Exception('The post destination file already exists')

    copyfile(os.getcwd() + '/template.md', path + '/template.md')


def copy_scripts(path):
    info('Copying main scripts')

    if not os.path.exists(os.getcwd() + '/scripts/process.py'):
        raise Exception('Post process script does not exists')

    copyfile(os.getcwd() + '/scripts/process.py', path + '/process.py')


def copy_utils(destpath):
    info('Copying util files')

    os.mkdir(join(destpath, 'utils/'))

    srcpath = join(os.getcwd(), 'utils/')
    dstpath = join(destpath, 'utils/')
    filestocopy = [f for f in listdir(srcpath) if isfile(join(srcpath, f))]
    [copyfile(join(srcpath, f), join(dstpath, f)) for f in filestocopy]


def create_links_file(destpath):
    info('Creating links.txt file')
    open(join(destpath, 'links.txt'), 'a').close()


def init(path, rootPath):
    info('Starting bootstraper')

    try:
        absolute_path = os.path.join(rootPath, path)
        create_work_dir_in_path(absolute_path)
        create_images_dirs(absolute_path)
        copy_post_template(absolute_path)
        copy_scripts(absolute_path)
        copy_utils(absolute_path)
        create_links_file(absolute_path)
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
                        default='d:/WS/BLOG/', dest='rootPath')

    args = parser.parse_args()

    init(args.path, args.rootPath)
