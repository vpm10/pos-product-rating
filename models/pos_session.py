from odoo import fields, models


class PosSession(models.Model):

    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()

        result['search_params']['fields'].append('rating')
        # print(result)
        return result
