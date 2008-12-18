from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from nrbc.literature import literatureMessageFactory as _

# -*- extra stuff goes here -*-

class ILiterature(Interface):
    """A Literature file that can be uploaded to the portal, with relevant metadata fields specified"""
