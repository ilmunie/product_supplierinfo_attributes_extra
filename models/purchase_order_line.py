from odoo import api, fields, models
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    @api.onchange('product_qty', 'product_uom')
    def _onchange_quantity(self):
        res = super(PurchaseOrderLine, self)._onchange_quantity()
        if not self.product_id:
            return res
        params = {'order_id': self.order_id}
        seller = self.product_id._select_seller(
            partner_id=self.partner_id,
            quantity=self.product_qty,
            date=self.order_id.date_order and self.order_id.date_order.date(),
            uom_id=self.product_uom,
            params=params)
        if seller and seller.variant_extra_ids:
            final_price = seller.get_final_price(self.product_id)
            self.price_unit = final_price
        return res

    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, company_id, supplier, po):
        res = super(PurchaseOrderLine, self)._prepare_purchase_order_line(product_id=product_id, product_qty=product_qty, product_uom=product_uom, company_id=company_id, supplier=supplier, po=po)
        partner = supplier.name
        uom_po_qty = product_uom._compute_quantity(product_qty, product_id.uom_po_id)
        seller = product_id.with_company(company_id)._select_seller(
            partner_id=partner,
            quantity=uom_po_qty,
            date=po.date_order and po.date_order.date(),
            uom_id=product_id.uom_po_id)
        if seller and seller.variant_extra_ids:
            final_price = seller.get_final_price(product_id)
            res['price_unit'] = final_price
        return res
