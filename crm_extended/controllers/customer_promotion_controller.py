import json

from odoo import http
from odoo.http import request


class CustomerPromotionController(http.Controller):
    @http.route(['/customers'], type='http', auth='public', website=True, csrf=False)
    def customers_page(self, search='', **kwargs):
        domain = []
        if search:
            domain = ['|', ('name', 'ilike', search), ('social_network_profile_ids.network_id.name', 'ilike', search)]

        customers = request.env['res.partner'].search(domain)
        return request.render('crm_extended.customer_promotion_template', {
            'customers': customers,
            'search': search
        })

