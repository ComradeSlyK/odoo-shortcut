# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from pathlib import Path


class File:

    def __init__(self, path):
        if isinstance(path, str):
            path = Path(path)
        self._path = path

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._path.name

    @property
    def path(self):
        return self._path


class Directory(File):

    def __init__(self, path, level=0):
        super().__init__(path)
        self.level = level
        self.subdirs = []
        self.files = []
        for sub in path.iterdir():
            if sub.is_dir():
                self.subdirs.append(Directory(sub, level + 1))
            else:
                self.files.append(File(sub))
