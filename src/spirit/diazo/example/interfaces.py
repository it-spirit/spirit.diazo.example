# -*- coding: utf-8 -*-
"""Common interface definitions for spirit.diazo.example."""

# zope imports
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISpiritDiazoExampleLayer(IDefaultBrowserLayer):
    """Marker interface that defines a Zope 3 browser layer."""
