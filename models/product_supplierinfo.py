from odoo import models, fields
class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    has_extras = fields.Boolean(string="¿Tiene extras?")
    variant_extra_ids = fields.One2many('supplier.variant.info', 'pricelist_id')
    def get_final_price(self, product=False):
        res = self
        final_price = res.price
        if not res.product_id and res.has_extras:
            if product.product_template_variant_value_ids and res.variant_extra_ids:
                for extra_to_check in res.variant_extra_ids:
                    add_extra = True
                    for attribute_value in extra_to_check.attribute_ids:
                        if attribute_value.id not in product.product_template_variant_value_ids.mapped('id'):
                            add_extra = False
                    if add_extra and extra_to_check.extra_amount:
                        final_price += extra_to_check.extra_amount
        return final_price