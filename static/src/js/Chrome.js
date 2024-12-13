odoo.define('pos_allow_employee_cash_move.chrome', function (require) {
    "use strict";
    const Chrome = require('point_of_sale.Chrome');
    const Registries = require('point_of_sale.Registries');

    const PosEmployee = (Chrome) =>
        class extends Chrome {
            showCashMoveButton() {
                return true
            }
        };
    Registries.Component.extend(Chrome, PosEmployee);

    return Chrome;
});