from __future__ import unicode_literals
from six import PY3

import logging
logger = logging.getLogger(__name__)

if PY3:
    def str_encode(value='', encoding=None, errors='strict'):
        return str(value, encoding, errors)


    def str_decode(value, encoding=None, errors='strict'):
        try:
            return bytes(value, encoding, errors).decode('utf-8')
        except:
            try:
               return value.decode(encoding)
            except:
                return str(value)
else:
    def str_encode(string='', encoding=None, errors='strict'):
        return unicode(string, encoding, errors)

    def str_decode(value='', encoding=None, errors='strict'):
        return value.decode(encoding, errors)
