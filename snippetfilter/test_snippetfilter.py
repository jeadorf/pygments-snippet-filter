#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from snippetfilter import SnippetFilter
from pygments import highlight
from pygments.lexers import TextLexer
from pygments.formatters import NullFormatter

sample_text = u"""1. line
2. line
3. line
4. line
5. line
"""

class SnippetFilterTest(unittest.TestCase):
    def setUp(self):
        self.lexer = TextLexer()
        self.formatter = NullFormatter()
    def test_noop(self):
        """Test no-operation feature."""
        self.lexer.add_filter(SnippetFilter())
        self.assertEqual(sample_text, highlight(sample_text, self.lexer, self.formatter))
    def test_firstline(self):
        """Extract the first line."""
        self.lexer.add_filter(SnippetFilter(toline=2))
        self.assertEqual(sample_text.split('\n')[0] + '\n', highlight(sample_text, self.lexer, self.formatter))
    def test_lastline(self):
        """Extract the last line."""
        self.lexer.add_filter(SnippetFilter(fromline=5))
        self.assertEqual(sample_text.split('\n')[4] + '\n', highlight(sample_text, self.lexer, self.formatter))
    def test_fromline(self):
        """Extract some of the last lines."""
        self.lexer.add_filter(SnippetFilter(fromline=3))
        exp = "\n".join(sample_text.split("\n")[2:])
        self.assertEqual(exp, highlight(sample_text, self.lexer, self.formatter))
    def test_toline(self):
        """Extract some of the first lines."""
        self.lexer.add_filter(SnippetFilter(toline=3))
        exp = "\n".join(sample_text.split("\n")[:2]) + "\n"
        self.assertEqual(exp, highlight(sample_text, self.lexer, self.formatter))
    def test_fromto(self):
        """Extract some of the lines in the middle."""
        self.lexer.add_filter(SnippetFilter(fromline=2,toline=4))
        exp = "\n".join(sample_text.split("\n")[1:3]) + "\n"
        self.assertEqual(exp, highlight(sample_text, self.lexer, self.formatter))
    def test_empty(self):
        """Extract nothing at all."""
        self.lexer.add_filter(SnippetFilter(fromline=3, toline=3))
        self.assertEqual('', highlight(sample_text, self.lexer, self.formatter))
    def test_section(self):
        """How python behaves on sublists like s[f:t]."""
        s = [0, 1, 2, 3]
        self.assertEqual([0, 1, 2, 3], s)
        self.assertEqual([0, 1, 2, 3], s[0:15])
        self.assertEqual([0, 1], s[0:2])
        self.assertEqual([2, 3], s[2:4])
        self.assertEqual(3, s[-1])
        self.assertEqual([3], s[-1:5])

suite = unittest.TestLoader().loadTestsFromTestCase(SnippetFilterTest)

if __name__ == '__main__':
    unittest.main()

