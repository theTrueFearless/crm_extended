from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    social_network_profile_ids = fields.One2many('crm_extended.social.network.profile', 'partner_id',
                                                 string='Social Profiles')
