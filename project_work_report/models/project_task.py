# -*- coding: utf-8 -*-
##############################################################################
# (c) 2015 bisnesmart
# License AGPL-3 - See LICENSE file on root folder for details
##############################################################################
from openerp import models, fields, api



class ProjectTasks(models.Model):
    _inherit = "project.task"

    customer_signature = fields.Binary("customer_signature")    