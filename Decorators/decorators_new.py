import functools

def do_thrice(func):
    def wrapper_do_thrice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_thrice

def do_thrice2(func):
    @functools.wraps(func)
    def wrapper_do_thrice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_thrice
