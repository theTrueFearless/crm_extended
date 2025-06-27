from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import ValidationError


@tagged('post_install', '-at_install')
class TestSocialNetworks(TransactionCase):
    """Tests for the CRM Extended module"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Models
        cls.SocialNetwork = cls.env['crm_extended.social.network']
        cls.SocialProfile = cls.env['crm_extended.social.network.profile']
        cls.Partner = cls.env['res.partner']

        # Networks
        cls.network1 = cls.SocialNetwork.create({
            'name': 'Twitter_TEST',
            'icon': 'iVBORw0KGgoAAAANSUhEUg=='  # Base64 mínimo
        })
        cls.network2 = cls.SocialNetwork.create({
            'name': 'LinkedIn_TEST',
            'icon': 'iVBORw0KGgoAAAANSUhEUg=='
        })

        # Partners
        cls.partner1 = cls.Partner.create({'name': 'Partner_TEST_1'})
        cls.partner2 = cls.Partner.create({'name': 'Partner_TEST_2'})

    def setUp(self):
        super().setUp()
        self.SocialProfile.search([]).unlink()

    def test_network_name_uniqueness(self):
        """Check that duplicate names are not allowed"""
        # Test 1: Must fail when creating duplicate name
        with self.assertRaises(ValidationError):
            self.SocialNetwork.create({
                'name': 'twitter_TEST',  # Same name in lowercase
                'icon': 'icon_data'
            })

        # Test 2: Different name must pass
        new_network = self.SocialNetwork.create({
            'name': 'Facebook_TEST',  # Unique name
            'icon': 'icon_data'
        })
        self.assertTrue(new_network.id)

    def test_url_validation(self):
        """Check URL validation"""
        # Case 1: Valid URL must be created
        valid_profile = self.SocialProfile.create({
            'url': 'https://twitter.com/user1',
            'partner_id': self.partner1.id,
            'network_id': self.network1.id
        })
        self.assertTrue(valid_profile.id)

        # Case 2: Invalid URL should fail
        with self.assertRaises(ValidationError):
            self.SocialProfile.create({
                'url': 'url_invalida',
                'partner_id': self.partner2.id,
                'network_id': self.network2.id
            })

    def test_completed_profile_computation(self):
        """Complete profile calculation"""

        self.assertFalse(self.partner1.completed_profile)

        self.SocialProfile.create({
            'url': 'https://twitter.com/user',
            'partner_id': self.partner1.id,
            'network_id': self.network1.id
        })

        self.assertFalse(self.partner1.completed_profile)

        """In environments with more social networks than those declared in the test, positive tests (assertTrue) will 
        not work because there will always be fewer profiles declared in the test than in the entire database."""

        """It is possible to perform a cleanup before starting the test but possible production data would be lost."""

        # self.SocialProfile.create({
        #     'url': 'https://linkedin.com/user',
        #     'partner_id': self.partner1.id,
        #     'network_id': self.network2.id
        # })
        #
        # self.assertTrue(self.partner1.completed_profile)
        #
        # self.partner1.social_network_profile_ids[0].unlink()
        # self.partner1.invalidate_recordset()
        # self.assertFalse(self.partner1.completed_profile)

