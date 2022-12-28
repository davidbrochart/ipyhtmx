# ipyhtmx

Build modern UIs in Jupyter with Python

## Installation

To install use pip:

    $ pip install ipyhtmx

For a development installation (requires [Node.js](https://nodejs.org) and [Yarn version 1](https://classic.yarnpkg.com/)),

    $ git clone https://github.com/davidbrochart/ipyhtmx.git
    $ cd ipyhtmx
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --overwrite --sys-prefix ipyhtmx
    $ jupyter nbextension enable --py --sys-prefix ipyhtmx

When actively developing your extension for JupyterLab, run the command:

    $ jupyter labextension develop --overwrite ipyhtmx

Then you need to rebuild the JS when you make a code change:

    $ cd js
    $ yarn run build

You then need to refresh the JupyterLab page when your javascript changes.
