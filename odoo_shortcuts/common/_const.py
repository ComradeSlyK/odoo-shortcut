# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from datetime import date
from pathlib import Path


# NB: every 'default' key must be a string! Conversion to other objects
# should be done by the args parser.
ARGS = {
    "application": {
        "args": [
            "--application"
        ],
        "kwargs": {
            "action": "store",
            "default": "False",
            "dest": "application",
            "help": "Is the module an app?"
        },
        "manifest": True,
        "type": "bool",
    },
    "author": {
        "args": [
            "--author"
        ],
        "kwargs": {
            "action": "store",
            "default": "Openforce",
            "dest": "author",
            "help": "Author(s)"
        },
        "manifest": True,
        "type": "str",
    },
    "auto-install": {
        "args": [
            "--auto-install"
        ],
        "kwargs": {
            "action": "store",
            "default": "False",
            "dest": "auto_install",
            "help": "Is the module auto-installable?"
        },
        "manifest": True,
        "type": "bool",
    },
    "category": {
        "args": [
            "--category"
        ],
        "kwargs": {
            "action": "store",
            "default": "Hidden",
            "dest": "category",
            "help": "Module category"
        },
        "manifest": True,
        "type": "str",
    },
    "conflicts": {
        "args": [
            "--conflicts"
        ],
        "kwargs": {
            "action": "store",
            "default": "",
            "dest": "conflicts",
            "help": "Module conflicts"
        },
        "manifest": True,
        "type": "list",
    },
    "copyright-header": {
        "args": [
            "--copyright-header"
        ],
        "kwargs": {
            "action": "store",
            "default": f"# Copyright {date.today().year}-TODAY"
                       f" Openforce Srls Unipersonale (www.openforce.it)\n"
                       f"# License LGPL-3.0 or later"
                       f" (https://www.gnu.org/licenses/lgpl).",
            "dest": "copyright_header",
            "help": "Copyright header"
        },
        "manifest": False,
        "type": "str",
    },
    "data": {
        "args": [
            "--data"
        ],
        "kwargs": {
            "action": "store",
            "default": "",
            "dest": "data",
            "help": "Module data"
        },
        "manifest": True,
        "type": "list",
    },
    "depends": {
        "args": [
            "--depends"
        ],
        "kwargs": {
            "action": "store",
            "default": "",
            "dest": "depends",
            "help": "Module dependencies"
        },
        "manifest": True,
        "type": "list",
    },
    "description": {
        "args": [
            "--description"
        ],
        "kwargs": {
            "action": "store",
            "default": "Module description: what does the module do?",
            "dest": "description",
            "help": "Module description"
        },
        "manifest": True,
        "type": "str",
    },
    "external-dependencies-bin": {
        "args": [
            "--ext-dep-bin"
        ],
        "kwargs": {
            "action": "store",
            "default": "",
            "dest": "external_deps_bin",
            "help": "Bin dependencies"
        },
        "manifest": True,
        "type": "list",
    },
    "external-dependencies-python": {
        "args": [
            "--ext-dep-py"
        ],
        "kwargs": {
            "action": "store",
            "default": "",
            "dest": "external_deps_python",
            "help": "Python dependencies"
        },
        "manifest": True,
        "type": "list",
    },
    "icon-path": {
        "args": [
            "--icon-path"
        ],
        "kwargs": {
            "action": "store",
            "default": str(
                Path(__file__).parent.joinpath('files/icon.png')
            ),
            "dest": "icon_path",
            "help": "Icon path (where the icon.png will be found)"
        },
        "manifest": False,
        "type": "path",
    },
    "installable": {
        "args": [
            "--installable"
        ],
        "kwargs": {
            "action": "store",
            "default": "True",
            "dest": "installable",
            "help": "Is module installable?"
        },
        "manifest": True,
        "type": "bool",
    },
    "license": {
        "args": [
            "--license"
        ],
        "kwargs": {
            "action": "store",
            "default": "LGPL-3",
            "dest": "license",
            "help": "Module license"
        },
        "manifest": True,
        "type": "str",
    },
    "module-name": {
        "args": [
            "-m",
            "--module-name"
        ],
        "kwargs": {
            "action": "store",
            "dest": "module_name",
            "help": "Module technical name (required!)",
            "required": True
        },
        "manifest": False,
        "type": "str",
    },
    "name": {
        "args": [
            "--name"
        ],
        "kwargs": {
            "action": "store",
            "default": "Module name",
            "dest": "name",
            "help": "Module name"
        },
        "manifest": True,
        "type": "str",
    },
    "odoo-version": {
        "args": [
            "--odoo-version"
        ],
        "kwargs": {
            "action": "store",
            "default": "X.X",
            "dest": "odoo_version",
            "help": "Odoo version"
        },
        "manifest": True,
        "type": "str",
    },
    "repo-path": {
        "args": [
            "-r",
            "--repo-path"
        ],
        "kwargs": {
            "action": "store",
            "default": str(Path('.').absolute()),
            "dest": "repo_path",
            "help": "Repo path"
        },
        "manifest": False,
        "type": "path",
    },
    "sequence": {
        "args": [
            "--sequence"
        ],
        "kwargs": {
            "action": "store",
            "default": "100",
            "dest": "sequence",
            "help": "Module sequence"
        },
        "manifest": True,
        "type": "int",
    },
    "structure": {
        "args": [
            "--structure"
        ],
        "kwargs": {
            "action": "store",
            "default": """
                controllers/,
                controllers/__init__.py,
                data/,
                i18n/,
                migrations/,
                models/,
                models/__init__.py,
                report/,
                report/__init__.py,
                report/templates/,
                security/,
                security/res_groups.xml,
                security/ir.model.access.csv,
                security/ir_rule.xml,
                static/,
                static/description/,
                static/src/,
                static/src/css/,
                static/src/img/,
                static/src/js/,
                tests/,
                views/,
                wizard/,
                wizard/__init__.py,
            """,
            "dest": "structure",
            "help": "Module structure"
        },
        "manifest": False,
        "type": "list",
    },
    "summary": {
        "args": [
            "--summary"
        ],
        "kwargs": {
            "action": "store",
            "default": "Short description",
            "dest": "summary",
            "help": "Module summary"
        },
        "manifest": True,
        "type": "str",
    },
    "website": {
        "args": [
            "--website"
        ],
        "kwargs": {
            "action": "store",
            "default": "http://www.openforce.it",
            "dest": "website",
            "help": "Module website"
        },
        "manifest": True,
        "type": "str",
    },
}
