# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates a whole new module within the specified repo
"""

import sys
from jinja2 import Environment, FileSystemLoader
from os.path import splitext
from pathlib import Path
from shutil import copy

from common.args_parser import parser


def add_icon(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """
    icon_path = data['icon_path']
    if icon_path:
        try:
            static_path = create_directory('static', module_path)
        except FileExistsError:
            static_path = module_path.joinpath('static')
        try:
            descr_path = create_directory('description', static_path)
        except FileExistsError:
            descr_path = static_path.joinpath('description')
        copy(icon_path, str(descr_path.joinpath('icon.png')))


def create_file(name, path):
    """
    :param str name: the module technical name
    :param pathlib.Path path: a ``pathlib.Path`` object representing the
        directory parent folder
    :return: a ``pathlib.Path`` object representing the file itself
    """
    file_path = path.joinpath(name)
    if file_path.exists():
        raise FileExistsError(
            f"File {name} in path {str(path)} already exists."
        )
    copyfile = ''
    if splitext(name.lower())[-1] == '.xml':
        copyfile = 'common/files/defaults/record.xml'
    elif name.lower() == 'ir.model.access.csv':
        copyfile = 'common/files/defaults/ir.model.access.csv'
    if copyfile:
        default = Path(__file__).parent.joinpath(copyfile)
        copy(str(default), str(file_path))
        return file_path
    with open(str(file_path), 'w'):
        return file_path


def create_directory(name, path):
    """
    :param str name: the module technical name
    :param pathlib.Path path: a ``pathlib.Path`` object representing the
        directory parent folder
    :return: a ``pathlib.Path`` object representing the directory itself
    """
    dir_path = path.joinpath(name)
    if dir_path.exists():
        raise FileExistsError(
            f"Directory {name} in path {str(path)} already exists."
        )
    dir_path.mkdir()
    return dir_path


def create_manifest(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """
    manifest_dir = Path(__file__).parent.joinpath('common/files')
    env = Environment(
        loader=FileSystemLoader(str(manifest_dir)),
        keep_trailing_newline=True,  # Allows the empty line at EOF
    )
    template = env.get_template('manifest.j2')
    with open(str(module_path.joinpath('__manifest__.py')), 'w') as manifest:
        manifest.write(template.render(data=data))


def create_module(name, path):
    """
    :param str name: the module technical name
    :param pathlib.Path path: a ``pathlib.Path`` object representing the module
        parent directory
    """
    if not (path.exists() and path.is_dir()):
        raise ValueError(
            f"Cannot create an Odoo module in path {str(path)}: it either"
            f" doesn't exist, or it's not a directory."
        )
    return create_directory(name, path)


def create_structure(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """
    # If keyword 'data' is not set, we'll update it according to the files
    # we'll find within the module structure
    update_data = data['data'] == '[]'
    data_to_argv = []
    for subs in map(lambda s: s.split('/'), data['structure']):
        is_directory = len(subs) > 1 and not subs[-1]
        for x in range(len(subs)):
            is_last_element = x == len(subs) - 1
            name = subs[x]
            if x:
                path = module_path.joinpath('/'.join(subs[:x]))
            else:
                path = module_path
            try:
                if is_last_element and is_directory:
                    create_directory(name, path)
                elif is_last_element:
                    if update_data and splitext(name.lower())[-1] != '.py':
                        data_to_argv.append('/'.join(subs))
                    create_file(name, path)
                else:
                    create_directory(name, path)
            except FileExistsError:
                pass
            except Exception:
                raise
    if data_to_argv:
        sys.argv.append('--data=' + ','.join(data_to_argv))
        data.update(parser.args_dict)


def generate_init_files(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """
    copyright_header = data['copyright_header'] + '\n'

    # Creating __init__.py files for most common directories
    valid_subdirs = []
    for subdir in ['controllers', 'models', 'report', 'wizard']:
        subdirpath = module_path.joinpath(subdir)
        if subdirpath.exists():
            with open(str(subdirpath.joinpath('__init__.py')), 'w') as init:
                init.write(copyright_header)
            valid_subdirs.append(subdir)

    if valid_subdirs:
        with open(str(module_path.joinpath('__init__.py')), 'w') as init:
            init.write(copyright_header + '\n')
            for subdir in valid_subdirs:
                init.write(f'from . import {subdir}\n')


def generate_module(name, path, data):
    """
    :param str name: the module technical name
    :param pathlib.Path path: a ``pathlib.Path`` object representing the module
        repository directory
    :param dict data: a dictionary containing every useful info about
    the module being created
    """
    module = create_module(name, path)
    create_structure(module, data)
    create_manifest(module, data)
    generate_init_files(module, data)
    add_icon(module, data)


if __name__ == '__main__':
    data = parser.args_dict
    generate_module(data['module_name'], data['repo_path'], data)
