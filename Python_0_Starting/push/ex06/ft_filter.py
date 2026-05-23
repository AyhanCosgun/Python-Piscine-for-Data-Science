def ft_filter(function, iter_inputs):
    """ Mimics the original
        filter(function or None, iterable) --> filter object
    """
    if function is None:
        return iter([item for item in iter_inputs if item])
    else:
        return iter([item for item in iter_inputs if function(item)])
