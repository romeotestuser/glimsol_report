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

from openerp.osv import fields, osv

class billing_statement(osv.osv):
    _inherit="account.billing"
    _name="account.billing"
    
    _columns={
              'approve_user_id':fields.many2one('res.users', 'Approved By', required=False), 
              'prepare_user_id':fields.many2one('res.users', 'Prepared By', required=False),
              'note': fields.text('Terms and conditions'),
              'verify_user_id':fields.many2one('res.users', 'Verified By', required=False), 
              
              

              
              }