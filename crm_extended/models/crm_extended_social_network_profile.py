from odoo import fields, models, api


class CrmExtendedSocialNetworkProfile(models.Model):
    _name = 'crm_extended.social.network.profile'
    _description = 'Social Network Profile of the customer'

    url = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, ondelete='cascade')
    network_id = fields.Many2one('crm_extended.social.network', string='Social Network', required=True)
    icon = fields.Binary(string="Icon", related='network_id.icon', store=False)
