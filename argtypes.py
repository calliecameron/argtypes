"""Helper functions for the 'type' argument of argparse's add_argument method."""

import argparse
import os.path

def positive_int(arg):
    """Test whether arg is a positive integer, and convert it to int"""
    i = int(arg)
    if i <= 0:
        raise argparse.ArgumentTypeError("'%d' is not a positive integer" % i)
    return i

class IntGreater(object):
    def __init__(self, val):
        super(IntGreater, self).__init__()
        self.val = val

    def __call__(self, arg):
        i = int(arg)
        if i <= self.val:
            raise argparse.ArgumentTypeError("'%d' is not greater than '%d'" % (i, self.val))
        return i

class IntLess(object):
    def __init__(self, val):
        super(IntLess, self).__init__()
        self.val = val

    def __call__(self, arg):
        i = int(arg)
        if i >= self.val:
            raise argparse.ArgumentTypeError("'%d' is not less than '%d'" % (i, self.val))
        return i

class IntGreaterEq(object):
    def __init__(self, val):
        super(IntGreaterEq, self).__init__()
        self.val = val

    def __call__(self, arg):
        i = int(arg)
        if i < self.val:
            raise argparse.ArgumentTypeError("'%d' is not greater than or equal to '%d'" % (i, self.val))
        return i

class IntLessEq(object):
    def __init__(self, val):
        super(IntLessEq, self).__init__()
        self.val = val

    def __call__(self, arg):
        i = int(arg)
        if i > self.val:
            raise argparse.ArgumentTypeError("'%d' is not less than or equal to '%d'" % (i, self.val))
        return i

def absolute_path(arg):
    return os.path.realpath(arg)

def existing_path(arg):
    if not os.path.exists(arg):
        raise argparse.ArgumentTypeError("path '%s' does not exist" % arg)
    return arg

def exitsing_absolute_path(arg):
    return os.path.realpath(existing_path(arg))

def existing_dir(arg):
    if not os.path.isdir(arg):
        raise argparse.ArgumentTypeError("directory '%s' does not exist" % arg)
    return arg

def exitsing_absolute_dir(arg):
    return os.path.realpath(existing_dir(arg))
