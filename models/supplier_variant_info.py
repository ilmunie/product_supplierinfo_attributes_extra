from odoo import models, fields, api

class ProductSupplierInfoVarianInfo(models.Model):
    _name = 'supplier.variant.info'

    extra_amount = fields.Float(string="Valor extra")
    pricelist_id = fields.Many2one('product.supplierinfo')
    attribute_ids = fields.Many2many(comodel_name='product.template.attribute.value', string="Atributos")
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
                ids = []
                for pp in rec.pricelist_id.product_tmpl_id.product_variant_ids:

                    #import pdb;
                        #pdb.set_trace()
                    ids.extend(pp.product_template_variant_value_ids.mapped('id'))
                return {'domain':{'attribute_ids': [('id','in',ids)]}}
            else:
                return