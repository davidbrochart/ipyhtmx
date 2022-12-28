from setuptools import setup
from pathlib import Path

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
)

JS_DIR = Path(__file__).resolve().parent / 'js'

# Representative files that should exist after a successful build
jstargets = [JS_DIR / 'dist' / 'index.js']

data_files_spec = [
    ('share/jupyter/nbextensions/ipyhtmx', 'ipyhtmx/nbextension', '*.*'),
    ('share/jupyter/labextensions/ipyhtmx', 'ipyhtmx/labextension', '**'),
    ('share/jupyter/labextensions/ipyhtmx', '.', 'install.json'),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'ipyhtmx.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(JS_DIR, npm=['yarn'], build_cmd='build:prod'),
    ensure_targets(jstargets),
)

# See setup.cfg for other parameters
setup(cmdclass=cmdclass)
