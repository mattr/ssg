import textwrap
from unittest import TestCase

from src.extracttitle import extract_title


class Test(TestCase):
    def test_extract_title(self):
        text = textwrap.dedent("""\n
        Some random text
        
        # The heading
        
        Some more text
        """).strip()
        actual = extract_title(text)
        self.assertEqual("The heading", actual)

    def test_extract_title_fail(self):
        with self.assertRaises(Exception):
            extract_title(textwrap.dedent("""\
            Some random text
            
            Some other text
            """).strip())
