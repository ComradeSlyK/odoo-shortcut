# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates every missing __init__.py and imports data within them
"""

from os.path import splitext

from common.args_parser import parser
from common.file_manager import Directory


def get_dirs_per_level(root):
    directories_per_level = {root.level: []}
    todo = [root]
    while todo:
        current_dir = todo.pop(0)
        if current_dir.level not in directories_per_level:
            directories_per_level[current_dir.level] = []
        directories_per_level[current_dir.level].append(current_dir)
        if current_dir.subdirs:
            todo.extend(current_dir.subdirs)
    return directories_per_level


def generate_init(data):
    root = Directory(data['repo_path'].joinpath(data['module_name']))
    header = data['copyright_header'] + '\n\n'
    for level, dirs in sorted(get_dirs_per_level(root).items(), reverse=True):
        for directory in dirs:
            pydirs = [
                d.name
                for d in directory.subdirs
                if d.path.joinpath('__init__.py').exists()
            ]
            pyfiles = [
                f.name
                for f in directory.files
                if splitext(f.name.lower())[-1] == '.py'
                if f.name.lower() not in ('__init__.py', '__manifest__.py')
            ]
            if pydirs or pyfiles:
                init_path = str(directory.path.joinpath('__init__.py'))
                with open(init_path, 'w') as init_file:
                    init_file.write(header)
                    for name in sorted(pydirs) + sorted(pyfiles):
                        if name.endswith('.py'):
                            name = name[:-3]
                        init_file.write(f"from . import {name}\n")


if __name__ == '__main__':
    generate_init(parser.args_dict)
