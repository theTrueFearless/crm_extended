from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    social_network_profile_ids = fields.One2many('crm_extended.social.network.profile', 'partner_id',
                                                 string='Social Profiles')
    completed_profile = fields.Boolean(compute='_compute_profile_social_complete', search='_search_completed_profile')

    @api.depends('social_network_profile_ids.network_id')
    def _compute_profile_social_complete(self):
        all_networks = self.env['crm_extended.social.network'].search([])
        all_network_ids = set(all_networks.ids)

        for record in self:
            customer_network_ids = set(record.social_network_profile_ids.mapped('network_id').ids)
            record.completed_profile = all_network_ids.issubset(customer_network_ids)

    def _search_completed_profile(self, operator, value):

        if operator not in ['=', '!=']:
            raise UserError(_("Unsupported operator for 'completed_profile'. Only '=' and '!=' are supported."))

        all_network_ids = set(self.env['crm_extended.social.network'].search([]).ids)
        all_partner_ids = []

        for record in self.search([]):
            partner_network_ids = set(record.social_network_profile_ids.mapped('network_id').ids)
            is_complete = all_network_ids.issubset(partner_network_ids)
            if (operator == '=' and is_complete == value) or (operator == '!=' and is_complete != value):
                all_partner_ids.append(record.id)

        return [('id', 'in', all_partner_ids)]
