"""Helper functions for the 'type' argument of argparse's add_argument method."""

import argparse
import pytimeparse.timeparse
import os.path

class IntCmp(object):
    """Check that arg is an integer satisfying a condition"""
    def __init__(self, val, description):
        super(IntCmp, self).__init__()
        self.val = int(val)
        self.description = description

    def valid(self, arg):
        """Boolean: does the arg satisfy the condition?"""
        raise NotImplementedError

    def __call__(self, arg):
        try:
            i = int(arg)
            if not self.valid(i):
                raise argparse.ArgumentTypeError("'%d' is not %s %d" % (i, self.description, self.val))
            return i
        except ValueError:
            raise argparse.ArgumentTypeError("'%s' is not an integer %s %d" % (arg, self.description, self.val))


class IntGreater(IntCmp):
    """Check that arg is greater than val"""
    def __init__(self, val):
        super(IntGreater, self).__init__(val, "greater than")

    def valid(self, arg):
        return arg > self.val

class IntLess(IntCmp):
    """Check that arg is less than val"""
    def __init__(self, val):
        super(IntLess, self).__init__(val, "less than")

    def valid(self, arg):
        return arg < self.val

class IntGreaterEq(IntCmp):
    """Check that arg is greater than or equal to val"""
    def __init__(self, val):
        super(IntGreaterEq, self).__init__(val, "greater than or equal to")

    def valid(self, arg):
        return arg >= self.val

class IntLessEq(IntCmp):
    """Check that arg is less than or equal to val"""
    def __init__(self, val):
        super(IntLessEq, self).__init__(val, "less than or equal to")

    def valid(self, arg):
        return arg <= self.val

positive_int = IntGreater(0)


def absolute_path(arg):
    """Convert arg to an absolute path"""
    return os.path.realpath(arg)

def existing_path(arg):
    """Make sure arg exists"""
    if not os.path.exists(arg):
        raise argparse.ArgumentTypeError("path '%s' does not exist" % arg)
    return arg

def existing_absolute_path(arg):
    """Make sure arg exists, and convert it to an absolute path"""
    return absolute_path(existing_path(arg))

def existing_dir(arg):
    """Make sure arg is a directory"""
    if not os.path.isdir(arg):
        raise argparse.ArgumentTypeError("directory '%s' does not exist" % arg)
    return arg

def existing_absolute_dir(arg):
    """Make sure arg is a directory, and convert it to an absolute path"""
    return absolute_path(existing_dir(arg))

def time_in_seconds(arg):
    """Parse arg as a time in seconds. See pytimeparse for the formats this
    accepts. Only accepts whole numbers of seconds."""
    try:
        return int(arg)
    except ValueError:
        i = pytimeparse.timeparse.timeparse(arg)
        if i is None or isinstance(i, float):
            raise argparse.ArgumentTypeError("'%s' is not a valid time" % arg)
        else:
            return i
