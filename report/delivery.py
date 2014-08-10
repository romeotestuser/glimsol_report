# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

from openerp.report import report_sxw
from openerp.netsvc import Service

for x in ['report.sale.shipping','report.picking.equipment.transfer']:
    try:
        del Service._services[x]
    except:
        pass

class shipping(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(shipping, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'line_number':self._get_product_line_number,
            'get_product_bundle_items':self._get_product_bundle_items,
        })
        
    def _get_product_bundle_items(self,product_id,context=None):
        cr=self.cr
        uid = self.uid
        #fetch connected product item entries

        cr.execute('select id from product_item where product_id = %s' % product_id)
        product_item_ids = [x[0] for x in cr.fetchall()]
        res = self.pool.get('product.item').read(cr,uid,product_item_ids,['item_id','qty_uom','uom_id'])
#         bundle_product_item_ids = [x[0] for x in cr.fetchall()]
#         product_dicts=self.pool.get('product.product').read(cr,uid,bundle_product_item_ids,['name'])
#         bundle_product_names = [product_dict['name'] for product_dict in product_dicts]
#         res = bundle_product_names
#         if context and 'mode' in context and context['mode'] == 'all':
#             res = [product_dict['id'] for product_dict in product_dicts]
        return res
            

    def _get_product_line_number(self,data,context=None):
        cr = self.cr
        #intigrate fetching of bundle items
        for datum in data:
            datum.bundle_items=self._get_product_bundle_items(datum.product_id.id)
            print "datum.bundle_items".upper(),datum.bundle_items            
        res = [(x+1,obj) for x,obj in enumerate(data)]
        return res        

#     def _get_product_line_number(self,data,context=None):
#         cr = self.cr
#         #intigrate fetching of bundle items
#         res = [(x+1,obj) for x,obj in enumerate(data)]
#         return res        
# 
report_sxw.report_sxw('report.picking.equipment.transfer','stock.picking','addons/glimsol_report/report/equipment_transfer.rml',parser=shipping)
report_sxw.report_sxw('report.picking.out.delivery.reciept','stock.picking.out','addons/glimsol_report/report/delivery_reciept.rml',parser=shipping)
report_sxw.report_sxw('report.picking.out.delivery.order','stock.picking.out','addons/glimsol_report/report/delivery_order.rml',parser=shipping)

report_sxw.report_sxw('report.sale.shipping.inherit','stock.picking','addons/glimsol_report/report/delivery_order.rml',parser=shipping)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: