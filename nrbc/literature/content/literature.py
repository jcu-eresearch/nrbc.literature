"""Definition of the Literature content type
"""

from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import ModifyPortalContent
from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.file import ATFile, ATFileSchema

from Products.Archetypes.public import StringField, StringWidget

from nrbc.literature import literatureMessageFactory as _
from nrbc.literature.interfaces import ILiterature
from nrbc.literature.config import PROJECTNAME

LiteratureSchema = schemata.ATContentTypeSchema.copy() + ATFileSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        name='authors',
        #storage = atapi.AnnotationStorage(),
        required=True,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"Authors"),
            description=_(u"The authors of the given piece of literature"),
            maxlength = 1000,
            size = 50,
        ),
    ),

    atapi.StringField(
        name='journal',
        #storage = atapi.AnnotationStorage(),
        required=False,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"Journal"),
            description=_(u"The journal from which the given piece of literature was taken"),
            maxlength = 255,
            size = 50,
        ),
    ),

    atapi.StringField(
        name='date',
        #storage = atapi.AnnotationStorage(),
        required=False,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"Publishing Date"),
            description=_(u"The date (or year only) that the work was published"),
	    size = 50,
        ),
    ),


    atapi.StringField(
        name='issue',
        #storage = atapi.AnnotationStorage(),
        required=False,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"Issue"),
            description=_(u"The issue of the journal or work that the piece of literature came from"),
	    maxlength = 80,
            size = 50,
        ),
    ),

    atapi.StringField(
        name='page',
        #storage = atapi.AnnotationStorage(),
        required=False,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"Page(s)"),
            description=_(u"The page or pages that the literature work originally resided within"),
            maxlength = 20,
            size = 50,
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

LiteratureSchema['title'].storage = atapi.AnnotationStorage()
LiteratureSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(LiteratureSchema, moveDiscussion=False)

class Literature(ATFile):
    """A Literature file that can be uploaded to the portal, with relevant metadata fields specified"""
    implements(ILiterature)

    portal_type = "Literature"
    schema = LiteratureSchema

    security = ClassSecurityInfo()

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    #security.declareProtected(ModifyPortalContent, 'setAuthor')
    #def setAuthor(self, value, **kwargs):
    #    field = self.getField('author')
    #    field.set(self, value, **kwargs) # set is ok




atapi.registerType(Literature, PROJECTNAME)
