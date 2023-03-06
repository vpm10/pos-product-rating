from odoo import fields, models, api


class ProductInherit(models.Model):
    _inherit = 'product.template'

    rating = fields.Selection(string="Rating",
                              selection=[
                                  ('1', 1), ('2', 2), ('3', 3),
                                  ('4', 4), ('5', 5)], default='1')
