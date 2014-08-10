


from openerp.osv import fields, osv
from openerp import netsvc

class account_invoice(osv.osv):
    _name = "account.invoice"
    _inherit = "account.invoice"
    
    _columns={
              'billing_type':fields.selection([('whole amount', 'Whole Amount'), 
                                               ('by percentage', 'Percentage'), 
                                               ('fixed amount', 'Fixed Amount'), 
                                               ('monthly by percentage', 'Percentage, Monthly Recurring'),
                                               ],    'Billing Type', select=True, readonly=False),
  'billing_extra_amount':fields.integer('Amount / Percentage'),
  'billing_months':fields.integer('No. of Months'),              
              }