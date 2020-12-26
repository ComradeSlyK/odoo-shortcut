# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import sys

from argparse import ArgumentParser
from pathlib import Path

from ._const import ARGS


class Parser(ArgumentParser):

    def _setup(self):
        for vals in ARGS.values():
            self.add_argument(*vals['args'], **vals['kwargs'])

    @property
    def args_dict(self):
        ns = self.parse_args()

        # The arguments dict will be created by formatting the args namespace
        # into a dict, and then its values will be re-adapted for our purposes
        ad = dict(ns._get_kwargs())

        maker = type(self)._val_maker
        for vals in ARGS.values():
            ad[vals['kwargs']['dest']] = maker(
                vals['type'],
                vals['kwargs']['dest'],
                ad[vals['kwargs']['dest']],
                vals['manifest']
            )

        return ad

    @classmethod
    def _bool_maker(cls, val, manifest):
        return bool(eval(val or ''))

    @classmethod
    def _int_maker(cls, val, manifest):
        return int(val)

    @classmethod
    def _list_maker(cls, val, manifest):
        if val and manifest:
            res = '['
            for c in val.split(','):
                if c.strip():
                    res += f'\n        \'{c.strip()}\','
            res += '\n    ]'
        elif val:
            res = [c.strip() for c in val.split(',' '') if c.strip()]
        else:
            res = '[]'
        return res

    @classmethod
    def _path_maker(cls, val, manifest):
        path = Path(val)
        if '~' in val:
            path = path.expanduser()
        return path.absolute()

    @classmethod
    def _str_maker(cls, val, manifest):
        return str(val or '')

    @classmethod
    def _val_maker(cls, argtype, fname, val, manifest):
        try:
            return getattr(cls, f'_{argtype}_maker')(val, manifest)
        except AttributeError:
            raise AttributeError(
                f"Cannot parse argument to type '{argtype}'. Make sure a"
                f" staticmethod f'_{argtype}_maker' is defined."
            )
        except Exception as e:
            raise ValueError(
                f"Invalid value for {fname}: '{val}'\n"
                f"Error: {str(e) or repr(e)}"
            )


parser = Parser()
parser._setup()
