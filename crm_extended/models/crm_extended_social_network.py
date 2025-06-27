from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class CrmExtendedSocialNetwork(models.Model):
    _name = 'crm_extended.social.network'
    _description = 'Social Network Nomenclator'

    name = fields.Char(required=True)
    icon = fields.Binary(required=True)

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([
                ('id', '!=', record.id),
                ('name', 'ilike', record.name.strip())
            ]) > 0:
                raise ValidationError(_(
                    "A social network named '%s' already exists (names are case-insensitive)."
                ) % record.name.strip())

