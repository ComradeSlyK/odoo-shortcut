# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Searches for non-.py objects and sets them into the __manifest__.py
"""

from os.path import splitext
from pathlib import Path

from common.args_parser import parser
from common.file_manager import get_dirtree
from common.tools import flatten


def generate_data_list(module_path):
    """
    :param pathlib.Path module_path: the module path as pathlib.Path object
    """
    manifest_path = module_path.joinpath('__manifest__.py')
    if not manifest_path.exists():
        # No __manifest__.py is found
        return

    # Retrieve files
    files = []
    for directory in flatten(get_dirtree(module_path).values()):
        for obj in directory.iterdir():
            if obj.is_dir():
                continue
            if splitext(obj.name.lower())[-1] != '.py':
                files.append(str(obj.relative_to(module_path)))

    # Retrieve lines in which existing data are already written
    data_rows = []
    with open(str(manifest_path), 'r') as manifest_file:
        manifest_data = dict(enumerate(manifest_file.readlines(), start=1))
    data_start = 0
    for n, r in manifest_data.items():
        if "'data'" in r:
            data_start = n
            break
    if data_start:
        data_rows = [data_start]
        data_end = data_start
        while data_end in manifest_data:
            if ']' in manifest_data[data_end]:
                break
            data_end += 1
            data_rows.append(data_end)

    # Case 1: 'data' key is already in __manifest__.py
    if data_rows:
        data = ''.join([manifest_data[r].strip() for r in data_rows])
        files += [
            f.replace('\'', '').strip()
            for f in data[data.index('[') + 1:data.index(']')].split(',')
            if f.replace('\'', '').strip()
            # This second 'if' removes files that no longer exist
            if Path(f.replace('\'', '').strip()).absolute().exists()
        ]
        pre_data_str = ''.join(
            [r for n, r in manifest_data.items() if n < min(data_rows)]
        )
        post_data_str = ''.join(
            [r for n, r in manifest_data.items() if n > max(data_rows)]
        )
        if files:
            data_str = "    'data': [\n"
            for f in sorted(set(files)):
                data_str += f"        '{f}',\n"
            data_str += "    ],\n"
        else:
            data_str = "    'data': [],\n"
        to_write = ''.join([pre_data_str, data_str, post_data_str])

    # Case 2: 'data' key isn't yet in __manifest__.py
    else:
        # Retrieve last valid line in __manifest__.py
        last_line = max(manifest_data)
        while '}' not in manifest_data[last_line]:
            last_line -= 1
        if files:
            data_str = "    'data': [\n"
            for f in sorted(set(files)):
                data_str += f"        '{f}',\n"
            data_str += "    ],\n"
        else:
            data_str = "    'data': [],\n"
        # Shift last_line one row lower and add data into its place
        manifest_data[last_line + 1] = manifest_data[last_line]
        manifest_data[last_line] = data_str
        to_write = ''.join(manifest_data.values())

    with open(str(manifest_path), 'w') as manifest_file:
        manifest_file.write(to_write)


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_data_list(mdata['module_path'])
