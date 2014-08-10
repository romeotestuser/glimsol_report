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
from openerp import netsvc
from openerp.netsvc import Service

for x in ['report.glimsol.billing.statement']:
    try:
        del Service._services[x]
    except:
        pass


from openerp.report import report_sxw

class billing(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(billing, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time, 
            'get_line':self._get_line,
            'get_total_si_amount':self._get_total_si_amount,
            'get_total_ticket_amount':self._get_total_ticket_amount,
            'get_user_ref':self._get_user_ref,
            })
        
    def _get_line(self,obj):
        res=[]
        
        return res
    
    def _get_total_si_amount(self,obj):
        res=[]
        
        return res
    
    def _get_total_ticket_amount(self,obj):
        res=[]
        
        return res    
    
    def _get_user_ref(self,obj,trigger):
        for target_trigger in ['sales executive','courier','customer']:
            if target_trigger != trigger:
                continue
            res = []
        
        return res    
        
report_sxw.report_sxw('report.glimsol.billing.statement', 'account.billing', 'addons/glimsol_report/report/billing_statement.rml', parser=billing, header="external")
        