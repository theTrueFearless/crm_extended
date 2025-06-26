from odoo import fields, models, api


class CrmExtendedSocialNetwork(models.Model):
    _name = 'crm_extended.social.network'
    _description = 'Social Network Nomenclator'

    name = fields.Char(required=True)
    icon = fields.Binary(required=True)

