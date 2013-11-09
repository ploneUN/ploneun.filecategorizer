from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok
from collective.grok import gs
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('ploneun.filecategorizer')

_ = MessageFactory

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)
    grok.name('ploneun.filecategorizer.upgrades')

    def getNonInstallableProducts(self):
        return [
            'ploneun.filecategorizer.upgrades',
        ]

gs.profile(name=u'default',
           title=u'ploneun.filecategorizer',
           description=_(u''),
           directory='profiles/default')
