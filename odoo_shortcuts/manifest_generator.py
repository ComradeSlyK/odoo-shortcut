# Copyright 2020-TODAY ComradeSlyK (gregorini.silvio@gmail.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

"""
Generates a whole new module within the specified repo
"""

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from common.args_parser import parser


def generate_manifest(module_path, data):
    """
    :param pathlib.Path module_path: the module as pathlib.Path object
    :param dict data: module data
    """
    manifest_dir = Path(__file__).parent.joinpath('common/files')
    env = Environment(
        loader=FileSystemLoader(str(manifest_dir)),
        keep_trailing_newline=True,  # Allows the empty line at EOF
    )
    template = env.get_template('manifest.j2')
    with open(str(module_path.joinpath('__manifest__.py')), 'w') as manifest:
        manifest.write(template.render(data=data))
    from data_list_generator import generate_data_list
    generate_data_list(module_path)


if __name__ == '__main__':
    mdata = parser.args_getter()
    generate_manifest(mdata['repo_path'].joinpath(mdata['module_name']), mdata)
