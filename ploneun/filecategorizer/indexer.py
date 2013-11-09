from Products.ATContentTypes.interfaces.file import IATFile
from plone.app.blob.interfaces import IATBlobFile
from plone.indexer import indexer


TYPES={
    'document': [
        'application/msword',
        'application/vnd.ms-word',
        'application/vnd.wordperfect',
        'application/vnd.sun.xml.writer',
        'application/vnd.sun.xml.writer.global',
        'application/vnd.sun.xml.writer.template',
        'application/vnd.stardivision.writer',
        'application/vnd.oasis.opendocument.text',
        'application/vnd.oasis.opendocument.text-template',
        'application/vnd.oasis.opendocument.text-web',
        'application/vnd.oasis.opendocument.text-master',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
    ],
    'spreadsheet': [
        'application/vnd.ms-excel',
        'application/vnd.stardivision.calc',
        'application/vnd.sun.xml.calc',
        'application/vnd.sun.xml.calc.template',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
        'application/vnd.oasis.opendocument.spreadsheet',
        'application/vnd.oasis.opendocument.spreadsheet-template'
    ],
    'presentation': [
        'application/vnd.ms-powerpoint',
        'application/vnd.stardivision.impress',
        'application/vnd.sun.xml.impress',
        'application/vnd.sun.xml.impress.template',
        'application/vnd.oasis.opendocument.presentation',
        'application/vnd.oasis.opendocument.presentation-template',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/vnd.openxmlformats-officedocument.presentationml.template'
   ] 
}

def get_type_string(mimetype):
    for k, v in TYPES.items():
        if mimetype in v:
            return k
    return None


def file_documenttype(obj):
    field = obj.getField('file')
    content_type = field.getContentType(obj)
    itemtype = get_type_string(content_type)
    if itemtype:
        return itemtype
    raise AttributeError(content_type)

@indexer(IATFile)
def atfile_documenttype(obj):
    return file_documenttype(obj)

@indexer(IATBlobFile)
def atblobfile_documenttype(obj):
    return file_documenttype(obj)


