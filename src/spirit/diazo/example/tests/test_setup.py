# -*- coding: utf-8 -*-
"""Test Setup of spirit.diazo.example."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# zope imports
from plone import api
from plone.browserlayer.utils import registered_layers

# local imports
from spirit.diazo.example import (
    config,
    testing,
)


CSS = [
    '++resource++spirit.diazo.example/main.css',
]

JS = [
    '++resource++spirit.diazo.example/main.js',
]


class TestSetup(unittest.TestCase):
    """Validate setup process for spirit.diazo.example."""

    layer = testing.SPIRIT_DIAZO_EXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

    def test_product_is_installed(self):
        """Validate that our product is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled(config.PROJECT_NAME))

    def test_addon_layer(self):
        """Validate that the browserlayer for our product is installed."""
        layers = [l.getName() for l in registered_layers()]
        self.assertIn('ISpiritDiazoExampleLayer', layers)

    # def test_cssregistry(self):
    #     """Validate the CSS file registration."""
    #     resource_ids = self.portal.portal_css.getResourceIds()
    #     for id in CSS:
    #         self.assertIn(id, resource_ids, '{0} not installed'.format(id))

    # def test_jsregistry(self):
    #     """Validate the JS file registration."""
    #     resource_ids = self.portal.portal_javascripts.getResourceIds()
    #     for id in JS:
    #         self.assertIn(id, resource_ids, '{0} not installed'.format(id))

    def test_plone_app_theming_installed(self):
        """Validate that plone.app.theming is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('plone.app.theming'))


class UninstallTestCase(unittest.TestCase):

    layer = testing.SPIRIT_DIAZO_EXAMPLE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

        qi = self.portal.portal_quickinstaller
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[config.PROJECT_NAME])

    def test_product_is_uninstalled(self):
        """Validate that our product is uninstalled."""
        qi = self.portal.portal_quickinstaller
        self.assertFalse(qi.isProductInstalled(config.PROJECT_NAME))

    def test_addon_layer_removed(self):
        """Validate that the browserlayer is removed."""
        layers = [l.getName() for l in registered_layers()]
        self.assertNotIn('ISpiritDiazoExampleLayer', layers)

    # def test_cssregistry(self):
    #     """Validate the CSS file unregistration."""
    #     resource_ids = self.portal.portal_css.getResourceIds()
    #     for id in CSS:
    #         self.assertNotIn(
    #             id, resource_ids,
    #             '{0} is still installed'.format(id),
    #         )

    # def test_jsregistry(self):
    #     """Validate the JS file unregistration."""
    #     resource_ids = self.portal.portal_javascripts.getResourceIds()
    #     for id in JS:
    #         self.assertNotIn(
    #             id, resource_ids,
    #             '{0} is still installed'.format(id),
    #         )
