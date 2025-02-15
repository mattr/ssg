import textwrap
from unittest import TestCase

from src.blocktoblocktype import block_to_block_type


class Test(TestCase):
    def test_headings(self):
        self.assertEqual("heading", block_to_block_type("# Heading 1"))
        self.assertEqual("heading", block_to_block_type("## Heading 2"))
        self.assertEqual("heading", block_to_block_type("### Heading 3"))
        self.assertEqual("heading", block_to_block_type("#### Heading 4"))
        self.assertEqual("heading", block_to_block_type("##### Heading 5"))
        self.assertEqual("heading", block_to_block_type("###### Heading 6"))
        self.assertEqual("paragraph", block_to_block_type("####### Heading 7"))

    def test_code(self):
        text = textwrap.dedent("""\
            ```
            This is some code
            ```""")
        self.assertEqual("code", block_to_block_type(text))

    def test_invalid_code(self):
        text = textwrap.dedent("""\
            ```
            This is some code
            """)
        self.assertEqual("paragraph", block_to_block_type(text))


    def test_quote(self):
        text = textwrap.dedent("""\
            > this is a valid quote
            > which spans multiple lines""")
        self.assertEqual("quote", block_to_block_type(text))

    def test_invalid_quote(self):
        text = textwrap.dedent("""\
            > this is a valid quote
            ! which spans multiple lines""")
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_unordered_list(self):
        text = textwrap.dedent("""\
            * a list
            * has items
            - and may have
            * different
            - list identifiers""")
        self.assertEqual("unordered_list", block_to_block_type(text))

    def test_invalid_unordered_list(self):
        text = textwrap.dedent("""\
            * a list
            * has items
            ! and may have
            different
            - list identifiers""")
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_ordered_list(self):
        text = textwrap.dedent("""\
            1. a list
            2. has items
            3. and may have
            4. different
            5. list identifiers""")
        self.assertEqual("ordered_list", block_to_block_type(text))

    def test_invalid_ordered_list(self):
        text = textwrap.dedent("""\
            1. a list
            2. has items
            3 and may have
            4..different
            list identifiers""")
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_invalid_ordering(self):
        text = textwrap.dedent("""\
            1. a list
            3. and may have
            2. has items
            4. different
            5. list identifiers""")
        self.assertEqual("paragraph", block_to_block_type(text))
