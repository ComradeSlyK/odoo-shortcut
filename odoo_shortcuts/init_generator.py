# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates every missing __init__.py and imports data within them
"""

from os.path import splitext

from common.args_parser import parser
from common.file_manager import get_dirtree


def generate_init(module_path):
    """
    :param pathlib.Path module_path: the module path as pathlib.Path object
    """
    files_to_skip = ('__init__.py', '__manifest__.py')
    for _, dirs in sorted(get_dirtree(module_path).items(), reverse=True):
        for directory in dirs:
            pydirs = []
            pyfiles = []
            for obj in directory.iterdir():
                if obj.is_dir() and obj.joinpath('__init__.py').exists():
                    pydirs.append(obj)
                elif splitext(obj.name.lower())[-1] == '.py' \
                        and obj.name.lower() not in files_to_skip:
                    pyfiles.append(obj)
            if pydirs or pyfiles:
                init_path = str(directory.joinpath('__init__.py'))
                with open(init_path, 'w') as init_file:
                    for obj in sorted(pydirs) + sorted(pyfiles):
                        name = obj.name
                        if name.endswith('.py'):
                            name = name[:-3]
                        init_file.write(f"from . import {name}\n")
    from copyright_header_generator import generate_copyright_header
    generate_copyright_header(
        module_path, parser.args_getter()['copyright_header']
    )


if __name__ == '__main__':
    generate_init(parser.args_getter()['module_path'])
