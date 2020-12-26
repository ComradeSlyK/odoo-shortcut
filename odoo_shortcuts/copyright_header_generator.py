# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Writes a copyright header into every .py file found within the module
"""


from os.path import splitext

from common.args_parser import parser
from common.file_manager import Directory


def generate_copyright_header(data):
    root = Directory(data['repo_path'].joinpath(data['module_name']))
    header = data['copyright_header'] + '\n'
    todo = [root]
    while todo:
        current_dir = todo.pop(0)
        for file in current_dir.files:
            if splitext(file.name.lower())[-1] == '.py':
                with open(str(file.path), 'r') as readfile:
                    filedata = readfile.read()
                if header.strip() in filedata:
                    continue
                with open(str(file.path), 'w') as writefile:
                    writefile.write(header)
                    if filedata:
                        if not filedata.startswith('\n'):
                            filedata = '\n' + filedata
                        writefile.write(filedata)


if __name__ == '__main__':
    generate_copyright_header(parser.args_dict)
