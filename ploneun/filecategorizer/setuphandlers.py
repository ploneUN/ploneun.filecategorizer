from collective.grok import gs
from ploneun.filecategorizer import MessageFactory as _

@gs.importstep(
    name=u'ploneun.filecategorizer', 
    title=_('ploneun.filecategorizer import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.filecategorizer.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
