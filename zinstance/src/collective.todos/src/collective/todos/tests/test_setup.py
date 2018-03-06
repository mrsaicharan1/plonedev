# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.todos.testing import COLLECTIVE_TODOS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.todos is properly installed."""

    layer = COLLECTIVE_TODOS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.todos is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.todos'))

    def test_browserlayer(self):
        """Test that ICollectiveTodosLayer is registered."""
        from collective.todos.interfaces import (
            ICollectiveTodosLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveTodosLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TODOS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get(userid=TEST_USER_ID).getRoles()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.todos'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.todos is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.todos'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTodosLayer is removed."""
        from collective.todos.interfaces import \
            ICollectiveTodosLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveTodosLayer,
           utils.registered_layers())
