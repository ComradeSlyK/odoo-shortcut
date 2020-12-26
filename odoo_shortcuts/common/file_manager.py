# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from pathlib import Path
from os import walk
from os.path import splitext
from shutil import copy


def create_directory(dir_path):
    """
    :param pathlib.Path dir_path: a ``pathlib.Path`` object representing the
        directory parent folder
    :return: a ``pathlib.Path`` object representing the directory itself
    """
    # Dir successful creation depends on the OS: if an error is raised,
    # the ``pathlib.Path`` will try to handle it; if it fails, it means
    # the OS itself is preventing the creation. Therefore, we'll simply
    # let the OS raise its proper error
    if dir_path.exists():
        raise FileExistsError(f"Directory {str(dir_path)} already exists.")
    dir_path.mkdir()
    return dir_path


def create_file(file_path):
    """
    :param pathlib.Path file_path: a ``pathlib.Path`` object representing the
        path to the file itself
    :return: a ``pathlib.Path`` object representing the file itself
    """
    if file_path.exists():
        raise FileExistsError(f"File {str(file_path)} already exists.")
    copyfile = ''
    if splitext(file_path.name.lower())[-1] == '.xml':
        copyfile = 'files/defaults/record.xml'
    elif file_path.name.lower() == 'ir.model.access.csv':
        copyfile = 'files/defaults/ir.model.access.csv'
    if copyfile:
        default = Path(__file__).parent.joinpath(copyfile)
        copy(str(default), str(file_path))
        return file_path
    with open(str(file_path), 'w'):
        return file_path


def get_dirtree(root_path):
    """
    :param pathlib.Path root_path: a ``pathlib.Path`` object representing the
        root directory to turn into a tree
    :return: a ``dict`` representing a mapping of the directory and its
        subdirectories per level, ie:

        root ('/opt/etc' ==> n = 3)
        |
        |___file1
        |
        |___sub1
        |   |___file2
        |   |___file3
        |
        |___sub2
        |   |___file4
        |   |___sub3
        |       |___file5
        |
        |___sub4

        becomes:
        {
            3: [root],
            4: [sub1, sub2, sub4],
            5: [sub3]
        }
    """
    tree = {}
    for p, _, _ in walk(root_path):
        path = Path(p).absolute()
        level = len(path._parts)
        try:
            tree[level].append(path)
        except KeyError:
            tree[level] = [path]
    return tree
