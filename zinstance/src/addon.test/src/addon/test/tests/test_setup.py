# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from addon.test.testing import ADDON_TEST_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that addon.test is properly installed."""

    layer = ADDON_TEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if addon.test is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'addon.test'))

    def test_browserlayer(self):
        """Test that IAddonTestLayer is registered."""
        from addon.test.interfaces import (
            IAddonTestLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAddonTestLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ADDON_TEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get(userid=TEST_USER_ID).getRoles()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['addon.test'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if addon.test is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'addon.test'))

    def test_browserlayer_removed(self):
        """Test that IAddonTestLayer is removed."""
        from addon.test.interfaces import \
            IAddonTestLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IAddonTestLayer,
           utils.registered_layers())
