import { DOMWidgetModel, DOMWidgetView } from '@jupyter-widgets/base';
import htmx from 'htmx.org';

export class HtmxModel extends DOMWidgetModel {
    defaults() {
      return {
        ...super.defaults(),
        _model_name : 'HtmxModel',
        _view_name : 'HtmxView',
        _model_module : 'ipyhtmx',
        _view_module : 'ipyhtmx',
        _model_module_version : '0.1.0',
        _view_module_version : '0.1.0',
        html : ''
      };
    }
  }

export class HtmxView extends DOMWidgetView {
    render() {
        this.value_changed();

        this.model.on('change:html', this.value_changed, this);
    }

    value_changed() {
        this.el.innerHTML = this.model.get('html');
        htmx.process(this.el);
    }
}
