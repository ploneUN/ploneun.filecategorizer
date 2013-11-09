from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class DocumentType(grok.GlobalUtility):
    grok.name('ploneun.filecategorizer.document_type')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
            'value': 'document',
            'title': 'Document',
        },
        {
            'value': 'spreadsheet',
            'title': 'Spreadsheet',
        },
        {
            'value': 'presentation',
            'title': 'Presentation',
        }
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
