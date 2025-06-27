{
    'name': 'Extended CRM',
    'version': '16.0',
    'summary': 'Social media management added to CRM',
    'description': '',
    'category': 'CRM',
    'author': 'Derly González',
    'website': 'Website',
    'license': 'LGPL-3',
    'depends': [
        'crm',
        'website'
        ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/website_setup.xml',
        # 'data/customers_promotion_page.xml',
        # views
        'views/customer_promotion_templates.xml',
        'views/crm_extended_social_network_views.xml',
        'views/crm_extended_social_network_profile_views.xml',
        'views/res_partner_views.xml',
        # menu
        'views/menu_views.xml'
    ],
    'demo': [
    ],
    'installable': True,
    "application": False,
    'auto_install': False
}
