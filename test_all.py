import unittest
from unittest.mock import patch # for functions with input
from pathlib import Path # to check for pycache

from external.execution import run_cmd
from external import cmds

class TestRunCmd(unittest.TestCase):
    ''' test all if statements in run_cmd from execution with the help of cmds '''


    @classmethod
    def setUpClass(cls): # overrides
        cls.test_counter = 0


    @classmethod
    def tearDownClass(cls): # also overrides default
        # copy paste from default values for reset
        with open('external/default_values.py', 'r') as f:
            default_values = f.read()
        with open('external/other_saved_data.py', 'w') as f:
            f.write(default_values)
        del f

        # delete all from saved_files
        with open('external/saved_files.py', 'w') as f:
            pass

        print('\n\nCarried out a reset.') # have to since some tests alter data, 
        # especially ones with the input function which asks for data.
        
        # e.g., change username to Pony overrides the previous username
        # so user name has to be reset afterwards

        # check for unnecessary folders
        pycache_path = Path("external") / "__pycache__" # pycache in external package
        if pycache_path.is_dir():
            print('\nFYI, a `__pycache__` folder was found in the `external` package.')
        
        pycache_path = Path.cwd() / "__pycache__" # pycache in curr working dir
        if pycache_path.is_dir():
            print('\nFYI, a `__pycache__` folder was found in the current working directory.')

        pycache_path = Path.cwd() / "build" # build folder is created in the process of building an exe
        if pycache_path.is_dir():
            print('\nFYI, a `build` folder was found in the current working directory.')

        pycache_path = Path.cwd() / "dist" # distribution folder is where an exe is defaultly present in
        if pycache_path.is_dir():
            print('\nFYI, a `dist` folder was found in the current working directory.')


    def setUp(self):
        TestRunCmd.test_counter += 1
        if TestRunCmd.test_counter == 1:
            print(f"Test # {TestRunCmd.test_counter}")
        else:
            print(f"\n\nTest # {TestRunCmd.test_counter}\n") # to avoid squishing
    

    @patch('builtins.input', side_effect=['4PurpleBlueberries', '3ricaceae5', '3'])
    def test_visit(self, mock_input):
        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.SEE_POP[0]], [], [], [])[0])

        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.BLUEBERRY[0]], [], [], [])[0]) # try first passcode
        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.BLUEBERRY[0]], [], [], [])[0]) # try second passcode

        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.NEWS[0]], [], [], [])[0])


    @patch('builtins.input', side_effect=['n', 'y', 'Pony'])
    def test_view(self, mock_input):
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.BOOKMARKS[0]], [], [], [])[0])
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.HELP[0]], [[['cmd_a'], ['cmd_b'], ['cmd_c']]], [], [])[0])
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.ALL_SAVED_FILES[0]], [], [], [['filename_a'], ['filename_b'], ['filename_c']])[0])

        # run and do not change username
        result: tuple[bool, str] = run_cmd([cmds.VIEW_CONTROLS[0], cmds.USERNAME[0]], [], [], [])

        self.assertTrue(result[0])
        self.assertIsInstance(result[1], str)

        # run and do change username
        result = run_cmd([cmds.VIEW_CONTROLS[0], cmds.USERNAME[0]], [], [], [])

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'Pony')


    def test_define(self):
        self.assertTrue(run_cmd([cmds.DEFINE[0], cmds.DEFINE[0]], [[cmds.DEFINE], []], [], [])[0])


    @patch('builtins.input', side_effect=['lorem ipsum', 'y', 'y'])
    def test_document_and_delete(self, mock_input):
        self.assertTrue(run_cmd([cmds.DOCUMENT[0], 'new thing'], [], [], [])[0])
        self.assertTrue(run_cmd([cmds.DELETE[0], 'new thing'], [], [], [['new thing', True, 'lorem ipsum']])[0])
        self.assertTrue(run_cmd([cmds.DELETE[0], cmds.ALL[0]], [], [], [['new thing', True, 'lorem ipsum'], ['also new thing', False, 'lorem ipsum']])[0])


    def test_message(self):
        self.assertTrue(run_cmd([cmds.MSG[0], cmds.ALL[0]], [], [], [])[0])
        self.assertTrue(run_cmd([cmds.MSG[0], cmds.NYOKA[0].lower()], [], [], [])[0])


    @patch('builtins.input', side_effect=['y', 'lorem ipsum'])
    def test_open(self, mock_input):
        self.assertTrue(run_cmd([cmds.OPEN[0], 'thing to edit'], [], [], [['thing to edit', True, 'edit this']])[0])
        self.assertTrue(run_cmd([cmds.OPEN[0], 'new thing'], [], [['new thing', True, 'lorem ipsum']], [])[0])


    @patch('builtins.input', side_effect=['3  '])
    def test_number_guessing(self, mock_input):
        result = run_cmd([cmds.VISIT_SITE[0], cmds.NUM_GUESSING[0]], [], [], [])

if __name__ == "__main__":
    unittest.main()