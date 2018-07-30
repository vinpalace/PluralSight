import unittest
import os

def analyze_text(filename):
    """Calculate the number of lines and characters in a file

    Args:
        filename: The name of the file to analyze

    Raises:
        IOError: If ''filename'' does not exist or can't be read.

    Returns:
        The number of lines of file
    """

    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return(lines, chars)

class TextAnalysisTests(unittest.TestCase):
    """Test for this"""

    def setUp(self):
        """Fixture that creates a file for the text methods to us"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether the nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass


    def test_function_runs(self):
        """Basis smoke test"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 131)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == "__main__":
    unittest.main()