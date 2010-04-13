#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments.filters import Filter
from pygments.util import get_int_opt
from pygments.token import Text
import sys
from itertools import izip, count

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
        for ttype, value in stream:
            lines = value.split('\n')
            for i, ln in izip(count(0), lines):
                if self.rd >= self.fr and self.rd < self.to:
                    if i < len(lines) - 1:
                        yield ttype, ln + '\n'
                    else:
                        yield ttype, ln
                self.rd += 1
            self.rd -= 1

