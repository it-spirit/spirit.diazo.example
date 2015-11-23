# -*- coding: utf-8 -*-
"""it-spirit Example Theme."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from spirit.diazo.example import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('spirit.diazo.example')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
