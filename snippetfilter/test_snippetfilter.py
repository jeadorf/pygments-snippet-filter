#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from snippetfilter import SnippetFilter
from pygments import highlight
from pygments.lexers import TextLexer
from pygments.lexers import CssLexer
from pygments.formatters import NullFormatter

class SnippetFilterTest(unittest.TestCase):
    def setUp(self):
        self.lexer = TextLexer()
        self.formatter = NullFormatter()
        self.text = u"""1. line
2. line
3. line
4. line
5. line
"""
        self.lines = self.text.split('\n')
    def test_noop(self):
        """Test no-operation feature."""
        self.lexer.add_filter(SnippetFilter())
        self.assertEqual(self.text, highlight(self.text, self.lexer, self.formatter))
    def test_firstline(self):
        """Extract the first line."""
        self.lexer.add_filter(SnippetFilter(toline=2))
        self.assertEqual(self.lines[0] + '\n', highlight(self.text, self.lexer, self.formatter))
    def test_snd_lastline(self):
        """Extract the second last line."""
        lineno = len(self.lines) - 2 
        self.lexer.add_filter(SnippetFilter(fromline=lineno+1))
        self.assertEqual(self.lines[lineno] + '\n', highlight(self.text, self.lexer, self.formatter))
    def test_fromline(self):
        """Extract some of the last lines."""
        self.lexer.add_filter(SnippetFilter(fromline=3))
        exp = "\n".join(self.lines[2:])
        self.assertEqual(exp, highlight(self.text, self.lexer, self.formatter))
    def test_toline(self):
        """Extract some of the first lines."""
        self.lexer.add_filter(SnippetFilter(toline=3))
        exp = "\n".join(self.lines[:2]) + "\n"
        self.assertEqual(exp, highlight(self.text, self.lexer, self.formatter))
    def test_fromto(self):
        """Extract some of the lines in the middle."""
        self.lexer.add_filter(SnippetFilter(fromline=2,toline=4))
        exp = "\n".join(self.lines[1:3]) + "\n"
        self.assertEqual(exp, highlight(self.text, self.lexer, self.formatter))
    def test_empty(self):
        """Extract nothing at all."""
        self.lexer.add_filter(SnippetFilter(fromline=3, toline=3))
        self.assertEqual('', highlight(self.text, self.lexer, self.formatter))
    def test_section(self):
        """How python behaves on sublists like s[f:t]."""
        s = [0, 1, 2, 3]
        self.assertEqual([0, 1, 2, 3], s)
        self.assertEqual([0, 1, 2, 3], s[0:15])
        self.assertEqual([0, 1], s[0:2])
        self.assertEqual([2, 3], s[2:4])
        self.assertEqual(3, s[-1])
        self.assertEqual([3], s[-1:5])

class CssSnippetFilterTest(SnippetFilterTest):
    def setUp(self):
        self.lexer = CssLexer()
        self.formatter = NullFormatter()
        self.text = """/* first line and comment */
div#test {
    font-size: 14px;
}

/* another
   comment */

.some {
    font-family: Monospace;
}
"""
        self.lines = self.text.split('\n')

text_suite = unittest.TestLoader().loadTestsFromTestCase(SnippetFilterTest)
css_suite  = unittest.TestLoader().loadTestsFromTestCase(CssSnippetFilterTest)
# All tests
test_suite = unittest.TestSuite([text_suite, css_suite])

if __name__ == '__main__':
    unittest.main()

