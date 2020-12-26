# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates a whole new module within the specified repo
"""

from json import load

from common.args_parser import parser
from common.file_manager import create_directory, create_file


def generate_module(module_path, data):
    """
    :param pathlib.Path module_path: a ``pathlib.Path`` object representing the
        module directory
    :param dict data: a dictionary containing every useful info about
    the module being created
    """
    create_directory(module_path)
    generate_structure(module_path, data)

    from icon_generator import generate_icon
    generate_icon(module_path, data['icon_path'])

    # This will trigger the data_list_generator script too
    from manifest_generator import generate_manifest
    generate_manifest(module_path, data)

    # This will trigger the copyright_header_generator script too
    from init_generator import generate_init
    generate_init(module_path)


def generate_structure(module_path, data):
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

    with open(data['structure_path'], 'r') as structure_json:
        structure_data = load(structure_json)
    for name, vals in structure_data.items():
        _create_structure(module_path.joinpath(name), vals)


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_module(mdata['repo_path'].joinpath(mdata['module_name']), mdata)
