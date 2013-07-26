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

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc




class emergency_contact(osv.osv):
    
   

    _name = 'emergency.contact'
    _description = 'Emergency Contact'
    _columns = {
        'employee_id': fields.many2one('hr.employee', 'Employee'),
        'partner_id': fields.many2one('res.partner', 'Customer', change_default=True, select=True, track_visibility='always' ),
        'name_e': fields.char('Contact Name', size=128, required=True, select=True),
        'street_e': fields.char('Street', size=128),
        'street2_e': fields.char('Street2', size=128),
        'email_e': fields.char('Email', size=240),
        'phone_e': fields.char('Phone', size=64),
        'fax_e': fields.char('Fax', size=64),
        'mobile_e': fields.char('Mobile', size=64),
        'zip_e': fields.char('Zip', size=24),
        'city_e': fields.char('City', size=128),
        'country_id_e': fields.many2one('res.country', 'Country'),
        'state_id_e': fields.many2one("res.country.state", 'State'),
    }
    
    
