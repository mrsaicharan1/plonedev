# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import addon.test


class AddonTestLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=addon.test)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'addon.test:default')


ADDON_TEST_FIXTURE = AddonTestLayer()


ADDON_TEST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ADDON_TEST_FIXTURE,),
    name='AddonTestLayer:IntegrationTesting'
)


ADDON_TEST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ADDON_TEST_FIXTURE,),
    name='AddonTestLayer:FunctionalTesting'
)


ADDON_TEST_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ADDON_TEST_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AddonTestLayer:AcceptanceTesting'
)
