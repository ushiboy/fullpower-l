class TerminatedException(Exception):
    pass


def raise_terminated():
    raise TerminatedException
