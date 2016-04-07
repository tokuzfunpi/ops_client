import json
import time
import hashlib
import six
import errno

def json_dump(_obj, indent = None, sort_key = False, ensure_ascii = True):
    return json.dumps(_obj, 
                      sort_keys = sort_key, 
                      indent = indent, 
                      ensure_ascii = ensure_ascii)
                      
def current_timestamp():
    return int(round(time.time()*1000))

class AttributeDict(dict): 
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def integrity_iter(iter, checksum):
    """
    Check image data integrity.

    :raises: IOError
    """
    md5sum = hashlib.md5()
    for chunk in iter:
        yield chunk
        if isinstance(chunk, six.string_types):
            chunk = six.b(chunk)
        md5sum.update(chunk)
    md5sum = md5sum.hexdigest()
    if md5sum != checksum:
        raise IOError(errno.EPIPE,
                      'Corrupt image download. Checksum was %s expected %s' %
                      (md5sum, checksum))
