# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Writes a copyright header into every .py file found within the module
"""

from os.path import splitext

from common.args_parser import parser
from common.file_manager import get_dirtree
from common.tools import flatten


def generate_copyright_header(module_path, header):
    """
    :param pathlib.Path module_path: the module path as pathlib.Path object
    :param str header: the header to be added
    """
    for current_dir in flatten(get_dirtree(module_path).values()):
        for obj in current_dir.iterdir():
            if splitext(obj.name.lower())[-1] == '.py':
                # Open the file in read mode to read previous file data
                with open(str(obj), 'r') as readfile:
                    filedata = readfile.read()
                if header.strip() in filedata:
                    # Current header already in data, skip file
                    continue
                # Open the file in write mode to update file data
                with open(str(obj), 'w') as writefile:
                    to_write = f"{header.strip()}\n"
                    if filedata:
                        to_write += f"\n{filedata.strip()}\n"
                    writefile.write(to_write)


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_copyright_header(mdata['module_path'], mdata['copyright_header'])
