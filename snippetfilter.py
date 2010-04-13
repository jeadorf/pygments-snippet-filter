#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments.filters import Filter
from pygments.util import get_int_opt
import sys

class SnippetFilter(Filter):
    """
    Extracts a code snippet.

    fromline    - the first line (included)
    toline      - the last line (excluded)
    """
    def __init__(self, **options):
        Filter.__init__(self, **options)
        # skip input to this delimiter
        self.fr = get_int_opt(options, 'fromline', 1) - 1
        # skip input after this delimiter
        self.to = get_int_opt(options, 'toline', sys.maxint) - 1
        # number of delimiters read
        self.rd = 0

    def filter(self, lexer, stream):
        addlf = False
        for ttype, value in stream:
            lines = value.split('\n')
            t = '\n'.join(lines[
                max(0, self.fr-self.rd):
                self.to-self.rd])
            if len(t) > 0:
                yield ttype, t
                addlf = (t[-1] != '\n')
            self.rd += len(lines) - 1
        if addlf:
            yield None, '\n'

