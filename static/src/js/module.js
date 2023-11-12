odoo.define('payment_method_visibility.module', function (require) {
    "use strict";

    var core = require('web.core');
    var ListRenderer = require('web.ListRenderer');
    var FormRenderer = require('web.FormRenderer');
    var TreeRenderer = require('web.TreeRenderer');

    var QWeb = core.qweb;
    var _t = core._t;

    ListRenderer.include({
        _renderRow: function (record) {
            var self = this;
            var $row = this._super.apply(this, arguments);
            var payment_method = record.data.payment_method_name;
            if (payment_method) {
                $row.addClass('payment-method-' + payment_method.toLowerCase());
            }
            return $row;
        },
    });

    FormRenderer.include({
        _renderTagLabel: function (node) {
            var result = this._super.apply(this, arguments);
            if (node.tag === 'field' && node.attrs.name === 'payment_method_name') {
                result.addClass('payment-method-label');
            }
            return result;
        },
    });

    TreeRenderer.include({
        _renderView: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                var payment_methods = self.state.data.map(function (record) {
                    return record.payment_method_name;
                });
                self.$el.addClass('payment-method-tree');
                self.$el.data('payment-methods', payment_methods);
            });
        },
    });

    return {
        ListRenderer: ListRenderer,
        FormRenderer: FormRenderer,
        TreeRenderer: TreeRenderer,
    };
});