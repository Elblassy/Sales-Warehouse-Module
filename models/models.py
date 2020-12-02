# -*- coding: utf-8 -*-


from odoo import models, fields, api
import logging
import codecs

_logger = logging.getLogger(__name__)


class WarehouseId(models.Model):
    _inherit = 'res.users'

    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', )
