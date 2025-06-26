from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    social_network_profile_ids = fields.One2many('crm_extended.social.network.profile', 'partner_id',
                                                 string='Social Profiles')
    completed_profile = fields.Boolean(compute='_compute_profile_social_complete')

    @api.depends('social_network_profile_ids.network_id')
    def _compute_profile_social_complete(self):
        all_networks = self.env['crm_extended.social.network'].search([])
        all_network_ids = set(all_networks.ids)

        for record in self:
            customer_network_ids = set(record.social_network_profile_ids.mapped('network_id').ids)
            record.completed_profile = all_network_ids.issubset(customer_network_ids)
