# -*- coding: utf-8 -*-
"""Test Layer for spirit.diazo.example."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)


class SpiritDiazoExampleLayer(PloneSandboxLayer):
    """Custom Test Layer for spirit.diazo.example."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import spirit.diazo.example
        self.loadZCML(package=spirit.diazo.example)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'spirit.diazo.example:default')


SPIRIT_DIAZO_EXAMPLE_FIXTURE = SpiritDiazoExampleLayer()


SPIRIT_DIAZO_EXAMPLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SPIRIT_DIAZO_EXAMPLE_FIXTURE,),
    name='SpiritDiazoExampleLayer:IntegrationTesting'
)


SPIRIT_DIAZO_EXAMPLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SPIRIT_DIAZO_EXAMPLE_FIXTURE,),
    name='SpiritDiazoExampleLayer:FunctionalTesting'
)


SPIRIT_DIAZO_EXAMPLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SPIRIT_DIAZO_EXAMPLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SpiritDiazoExampleLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='spirit.diazo.example:Robot')
