# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from argparse import ArgumentParser
from pathlib import Path

from .args_parser_params import _args_getter


class Parser(ArgumentParser):

    def _setup(self):
        for vals in _args_getter().values():
            self.add_argument(*vals['args'], **vals['kwargs'])

    def args_getter(self):
        ns = self.parse_args()

        # The arguments dict will be created by formatting the args namespace
        # into a dict, and then its values will be re-adapted for our purposes
        ad = dict(ns._get_kwargs())

        maker = type(self)._val_maker
        for vals in _args_getter().values():
            ad[vals['kwargs']['dest']] = maker(
                vals['type'],
                vals['kwargs']['dest'],
                ad[vals['kwargs']['dest']],
                vals['manifest']
            )

        # Custom behaviour: set the module name from its technical name
        from .args_parser_params import NAME
        if ad['name'] == NAME:
            ad['name'] = ' '.join(
                [w.title() for w in ad['module_name'].split('_')]
            )

        # Custom behaviour: add the module path even if not defined in script
        # arguments namespace
        ad['module_path'] = ad['repo_path'].joinpath(ad['module_name'])

        # Custom behaviour: set the version number with exactly 5 non-empty
        # values
        from .args_parser_params import VERSION
        version_vals = VERSION.split('.')
        version = ad['version'].split('.')
        if len(version) < 5:
            version.extend(version_vals[len(version):])
        elif len(version) > 5:
            version = version[:5]
        new_version = []
        for v, w in zip(version, version_vals):
            try:
                new_version.append(str(int(v if v.strip() else w)))
            except ValueError:
                new_version.append(v if v.strip() else w)
        ad['version'] = '.'.join(new_version)

        return ad

    @classmethod
    def _bool_maker(cls, val, *a, **kw):
        return bool(eval(val or ''))

    @classmethod
    def _int_maker(cls, val, *a, **kw):
        return int(val)

    @classmethod
    def _list_maker(cls, val, manifest, *a, **kw):
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
    def _path_maker(cls, val, *a, **kw):
        path = Path(val)
        if '~' in val:
            path = path.expanduser()
        return path.absolute()

    @classmethod
    def _str_maker(cls, val, *a, **kw):
        return str(val or '')

    @classmethod
    def _val_maker(cls, argtype, fname, val, manifest, *a, **kw):
        try:
            return getattr(
                cls, f'_{argtype}_maker')(val=val, manifest=manifest, *a, **kw
                                          )
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
