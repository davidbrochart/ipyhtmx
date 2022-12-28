import ipywidgets as widgets
from traitlets import Unicode
from ._version import NPM_PACKAGE_RANGE

@widgets.register
class Htmx(widgets.DOMWidget):
    """An example widget."""

    # Name of the widget view class in front-end
    _view_name = Unicode('HtmxView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('HtmxModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('ipyhtmx').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('ipyhtmx').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode(NPM_PACKAGE_RANGE).tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode(NPM_PACKAGE_RANGE).tag(sync=True)

    html = Unicode().tag(sync=True)
