

from openerp.osv import fields, osv
from openerp import netsvc


class sale_order(osv.osv):
    _name = "sale.order"
    _inherit = "sale.order"
    
    _columns={
              'billing_type':fields.selection([('whole amount', 'Whole Amount'), 
                                               ('by percentage', 'Percentage'), 
                                               ('fixed amount', 'Fixed Amount'), 
                                               ('monthly by percentage', 'Percentage, Monthly Recurring'),
                                               ],    'Billing Type', select=True, readonly=False),
  'billing_extra_amount':fields.integer('Amount / Percentage'),
  'billing_months':fields.integer('No. of Months'),              
              }
    def print_quotation(self, cr, uid, ids, context=None):
        '''
        This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        wf_service = netsvc.LocalService("workflow")
        wf_service.trg_validate(uid, 'sale.order', ids[0], 'quotation_sent', cr)
        datas = {
                 'model': 'sale.order',
                 'ids': ids,
                 'form': self.read(cr, uid, ids[0], context=context),
        }
        return {'type': 'ir.actions.report.xml', 'report_name': 'sale.order.inherit', 'datas': datas, 'nodestroy': True}
    _defaults = {  
        'billing_type': 'whole amount',  
        }
    
    def get_product_bundle(self,cr,uid,product_id,context=None):
        #fetch connected product item entries
        cr.execute('select product_id from product_item where product_id = %s' % product_id)
        bundle_product_item_ids = [x[0] for x in cr.fetchall()]
        product_dicts=self.pool.get('product.product').read(cr,uid,bundle_product_item_ids,['name'])
        bundle_product_names = [product_dict['name'] for product_dict in product_dicts]
        res = bundle_product_names
        if context and 'mode' in context and context['mode'] == 'all':
            res = [product_dict['id'] for product_dict in product_dicts]
        return res

sale_order()    