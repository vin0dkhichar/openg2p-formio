from odoo import fields, models, api

class Inherit_Program(models.Model):
    _inherit="g2p.program"
    
    self_service_portal_frm=fields.Many2one(
        "formio.builder",
        string="Program Form",
    )