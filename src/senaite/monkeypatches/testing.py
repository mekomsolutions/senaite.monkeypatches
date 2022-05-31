# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.monkeypatches


class SenaiteMonkeypatchesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.monkeypatches)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.monkeypatches:default')


SENAITE_MONKEYPATCHES_FIXTURE = SenaiteMonkeypatchesLayer()


SENAITE_MONKEYPATCHES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_MONKEYPATCHES_FIXTURE,),
    name='SenaiteMonkeypatchesLayer:IntegrationTesting',
)


SENAITE_MONKEYPATCHES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_MONKEYPATCHES_FIXTURE,),
    name='SenaiteMonkeypatchesLayer:FunctionalTesting',
)


SENAITE_MONKEYPATCHES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_MONKEYPATCHES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteMonkeypatchesLayer:AcceptanceTesting',
)
