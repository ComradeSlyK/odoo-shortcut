# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates a whole new module within the specified repo
"""

import sys
from jinja2 import Environment, FileSystemLoader
from json import load
from os.path import splitext
from pathlib import Path

from common.args_parser import parser
from common.file_manager import create_directory, create_file


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


def create_structure(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """

    def _create_structure(_path, _vals):
        if _vals['type'] == 'dir':
            create_directory(_path)
            for k, v in _vals.items():
                if k != 'type':
                    _create_structure(_path.joinpath(k), v)
        elif _vals['type'] == 'file':
            create_file(_path)
            if update_data and splitext(str(_path))[-1].lower() != '.py':
                data_to_argv.append(str(_path.relative_to(module_path)))

    # If keyword 'data' is not set, we'll update it according to the files
    # we'll find within the module structure
    update_data = data['data'] == '[]'
    data_to_argv = []
    with open(data['structure_path'], 'r') as structure_json:
        structure_data = load(structure_json)
    for name, vals in structure_data.items():
        _create_structure(module_path.joinpath(name), vals)

    if data_to_argv:
        sys.argv.append('--data=' + ','.join(data_to_argv))
        data.update(parser.args_getter())


def generate_module(module_path, data):
    """
    :param pathlib.Path module_path: a ``pathlib.Path`` object representing the
        module directory
    :param dict data: a dictionary containing every useful info about
    the module being created
    """
    create_directory(module_path)
    create_structure(module_path, data)
    create_manifest(module_path, data)
    from init_generator import generate_init
    generate_init(module_path)
    from icon_generator import generate_icon
    generate_icon(module_path, data['icon_path'])


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_module(mdata['repo_path'].joinpath(mdata['module_name']), mdata)
