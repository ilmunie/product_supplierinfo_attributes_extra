from odoo import models, fields, api

class ProductSupplierInfoVarianInfo(models.Model):
    _name = 'supplier.variant.info'

    attribute_ids = fields.Many2many(comodel_name='product.template.attribute.value')
    extra_amount = fields.Float()
    pricelist_id = fields.Many2one('product.supplierinfo')
    product_template_id = fields.Many2one(related='pricelist_id.product_tmpl_id',store=True,readonly=False)

    def name_get(self):
        res = []
        for rec in self:
            name = ''
            for attribute in rec.attribute_ids:
                if name:
                    name += " | "
                name += attribute.display_name
            name += ': +' + str(rec.extra_amount)
            res.append((rec.id, name))
        return res

    @api.onchange('product_template_id')
    def _onchange_pricelist_product_tmpl(self):
        for rec in self:
            if rec.pricelist_id and rec.pricelist_id.product_tmpl_id:
                return {'domain':{'attribute_ids': [('product_tmpl_id','=',rec.pricelist_id.product_tmpl_id.id)]}}
            else:
                return