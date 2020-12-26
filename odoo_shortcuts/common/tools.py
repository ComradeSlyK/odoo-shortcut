# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from collections import Iterable


def flatten(iterable):
    """
    Flatten an iterable of elements into a unique list
    Author: Christophe Simonis (christophe@tinyerp.com)
    """
    r = []
    for e in iterable:
        if isinstance(e, (bytes, str)) or not isinstance(e, Iterable):
            r.append(e)
        else:
            r.extend(flatten(e))
    return r
