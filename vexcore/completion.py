from .sourcekitd.capi import Config, UIdent
from .sourcekitd.request import request_sync

class Completion():
    request_key = "source.request.codecomplete"

    def __init__(self, text=None, source_file=None):
        self.source_file = source_file
        self.text = text

    def completion_at_offset(self, byte_offset):
        req = { 
                'key.request': UIdent(self.request_key),
                'key.offset': byte_offset
                }
        if not self.text == None:
            req['key.sourcetext'] = self.text
        elif not self.file == None:
            req['key.sourcefile'] = self.source_file
        else:
            raise RuntimeError("Must do completion on file or text")
        return request_sync(req)


