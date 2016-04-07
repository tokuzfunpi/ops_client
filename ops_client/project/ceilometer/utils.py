import six

def merge_nested_dict(dest, source, depth=0):
    for (key, value) in six.iteritems(source):
        if isinstance(value, dict) and depth:
            merge_nested_dict(dest[key], value,
                              depth=(depth - 1))
        else:
            dest[key] = value