# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from datetime import date
from pathlib import Path

COMMON_DIR = Path(__file__).absolute().parent

# NB: every 'default' key must be a string! Conversion to other objects
# should be done by the args parser.
APPLICATION = "False"
AUTHOR = "Openforce"
AUTO_INSTALL = "False"
CATEGORY = "Hidden"
CONFLICTS = ""
COPYRIGHT = f"# Copyright {date.today().year}-TODAY Openforce Srls" \
            f" Unipersonale (www.openforce.it)\n" \
            f"# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl)."
DATA = ""
DEPENDS = ""
DESCRIPTION = "Long description: what does the module do?"
EXT_DEP_BIN = ""
EXT_DEP_PY = ""
ICON_PATH = str(COMMON_DIR.joinpath("files/icon.png"))
INSTALLABLE = "True"
LICENSE = "LGPL-3"
NAME = "Module name"
ODOO_VERSION = "X.X"
# NB: if not manually specified, we use the path from which the scripts are
# being executed
REPO_PATH = Path(".").absolute()
SEQUENCE = "100"
STRUCTURE_PATH = str(COMMON_DIR.joinpath("files/structure.json"))
SUMMARY = "Short description"
WEBSITE = "http://www.openforce.it"


def _args_getter():
    return {
        "application": {
            "args": [
                "--application"
            ],
            "kwargs": {
                "action": "store",
                "default": APPLICATION,
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
                "default": AUTHOR,
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
                "default": AUTO_INSTALL,
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
                "default": CATEGORY,
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
                "default": CONFLICTS,
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
                "default": COPYRIGHT,
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
                "default": DATA,
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
                "default": DEPENDS,
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
                "default": DESCRIPTION,
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
                "default": EXT_DEP_BIN,
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
                "default": EXT_DEP_PY,
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
                "default": ICON_PATH,
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
                "default": INSTALLABLE,
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
                "default": LICENSE,
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
                "default": NAME,
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
                "default": ODOO_VERSION,
                "dest": "odoo_version",
                "help": "Odoo version"
            },
            "manifest": True,
            "type": "str",
        },
        "sequence": {
            "args": [
                "--sequence"
            ],
            "kwargs": {
                "action": "store",
                "default": SEQUENCE,
                "dest": "sequence",
                "help": "Module sequence"
            },
            "manifest": True,
            "type": "int",
        },
        "structure-path": {
            "args": [
                "--structure-path"
            ],
            "kwargs": {
                "action": "store",
                "default": STRUCTURE_PATH,
                "dest": "structure_path",
                "help": "Path to module structure .json file"
            },
            "manifest": False,
            "type": "path",
        },
        "summary": {
            "args": [
                "--summary"
            ],
            "kwargs": {
                "action": "store",
                "default": SUMMARY,
                "dest": "summary",
                "help": "Module summary"
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
                "default": str(REPO_PATH),
                "dest": "repo_path",
                "help": "Repo path"
            },
            "manifest": False,
            "type": "path",
        },
        "website": {
            "args": [
                "--website"
            ],
            "kwargs": {
                "action": "store",
                "default": WEBSITE,
                "dest": "website",
                "help": "Module website"
            },
            "manifest": True,
            "type": "str",
        },
    }
