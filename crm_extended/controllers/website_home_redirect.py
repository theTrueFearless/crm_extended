from odoo import http
from odoo.http import request


class WebsiteRedirectController(http.Controller):

    @http.route('/', type='http', auth="public", website=True)
    def homepage_redirect(self, **kw):
        # Redirige al listado de clientes sociales
        return request.redirect('/customers')