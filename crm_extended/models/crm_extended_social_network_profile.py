from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class CrmExtendedSocialNetworkProfile(models.Model):
    _name = 'crm_extended.social.network.profile'
    _description = 'Social Network Profile of the customer'

    url = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, ondelete='cascade')
    network_id = fields.Many2one('crm_extended.social.network', string='Social Network', required=True)
    icon = fields.Binary(string="Icon", related='network_id.icon', store=False)

    _sql_constraints = [
        ('unique_profile', 'UNIQUE(partner_id, network_id)',
         _('Each customer can only have one profile per social network!')),
    ]

    @api.constrains('url')
    def _check_valid_url(self):
        for record in self:
            if self.url:
                if not record.url.startswith(('http://', 'https://')) or not "." in record.url:
                    raise ValidationError(_("URL must start with http:// or https:// and have '.' inside"))
