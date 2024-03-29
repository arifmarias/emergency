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

from openerp.osv import fields,osv

class hr_employee(osv.osv):

    """ Inherits partner and adds Tasks information in the partner form """
    _inherit = 'hr.employee'
    _columns = {
        'econtact_ids': fields.one2many('emergency.contact', 'employee_id', 'Emergency Contact'),
    }

    

hr_employee()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
