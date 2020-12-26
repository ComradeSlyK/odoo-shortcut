# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Adds the icon to the specified module
"""

from shutil import copy

from common.args_parser import parser
from common.file_manager import create_directory


def generate_icon(module_path, icon_path):
    """
    :param pathlib.Path module_path: the module path as pathlib.Path object
    :param pathlib.Path icon_path: the src icon path as pathlib.Path object
    """
    try:
        static_path = create_directory(module_path.joinpath('static'))
    except FileExistsError:
        static_path = module_path.joinpath('static')
    try:
        descr_path = create_directory(static_path.joinpath('description'))
    except FileExistsError:
        descr_path = static_path.joinpath('description')
    copy(str(icon_path), str(descr_path.joinpath('icon.png')))


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_icon(mdata['module_path'], mdata['icon_path'])
