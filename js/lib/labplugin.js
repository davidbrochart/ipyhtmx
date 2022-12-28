import {HtmxModel, HtmxView, version} from './index';
import {IJupyterWidgetRegistry} from '@jupyter-widgets/base';

export const helloWidgetPlugin = {
  id: 'ipyhtmx:plugin',
  requires: [IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipyhtmx',
          version: version,
          exports: { HtmxModel, HtmxView }
      });
  },
  autoStart: true
};

export default helloWidgetPlugin;
