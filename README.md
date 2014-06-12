Argtypes
========

The `type` argument of Argparse's `add_argument` method lets the parser do validation and type conversion of arguments. This module provides a few convenient helper functions for use with `type`.

    import argparse
    import argtypes

    parser = argparse.ArgumentParser(description="Argtypes example")
    parser.add_argument("num_runs", type=argtypes.positive_int)
    parser.add_argument("dir", type=argtypes.existing_dir)
    args = parser.parse_args()
    print args

Requirements
------------

`pytimeparse` (which requires `future`):

    pip install pytimeparse future

Setup
-----

1. Clone this repo.
2. Add it to your PYTHONPATH.
