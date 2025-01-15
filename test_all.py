import unittest
from unittest.mock import patch # for functions with input
from external.execution import run_cmd
from external import cmds

class TestRunCmd(unittest.TestCase):
    ''' test all if statements in run_cmd from execution with the help of cmds '''

    @classmethod
    def setUpClass(cls): # overrides
        cls.test_counter = 0

    @classmethod
    def tearDownClass(cls):
        with open('external/default_values.py', 'r') as f:
            default_values = f.read()

        with open('external/other_saved_data.py', 'w') as f:
            f.write(default_values)

        print('\n\nCarried out a reset.')

    def setUp(self):
        TestRunCmd.test_counter += 1
        if TestRunCmd.test_counter == 1:
            print(f"Test # {TestRunCmd.test_counter}")
        else:
            print(f"\n\nTest # {TestRunCmd.test_counter}\n") # to avoid squishing
    
    @patch('builtins.input', side_effect=['4PurpleBlueberries', '3ricaceae5'])
    def test_visit(self, mock_input):
        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.SEE_POP[0]], [], [], [], [])[0])

        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.BLUEBERRY[0]], [], [], [], [])[0]) # try first passcode
        self.assertTrue(run_cmd([cmds.VISIT_SITE[0], cmds.BLUEBERRY[0]], [], [], [], [])[0]) # try second passcode

    @patch('builtins.input', side_effect=['n', 'y', 'Pony'])
    def test_view(self, mock_input):
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.BOOKMARKS[0]], [], [], [], [])[0])
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.HELP[0]], [], [['cmd_a', 'cmd_b', 'cmd_c'], []], [], [])[0])
        self.assertTrue(run_cmd([cmds.VIEW_CONTROLS[0], cmds.ALL_SAVED_FILES[0]], [], [], [], [['filename_a'], ['filename_b'], ['filename_c']])[0])

        # run and do not change username
        result: tuple[bool, str] = run_cmd([cmds.VIEW_CONTROLS[0], cmds.USERNAME[0]], [], [], [], [])

        self.assertTrue(result[0])
        self.assertIsInstance(result[1], str)

        # run and do change username
        result = run_cmd([cmds.VIEW_CONTROLS[0], cmds.USERNAME[0]], [], [], [], [])

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'Pony')

    def test_define(self):
        self.assertTrue(run_cmd([cmds.DEFINE[0], cmds.DEFINE[0]], [[cmds.DEFINE], []], [], [], [])[0])

    @patch('builtins.input', side_effect=['lorem ipsum', 'y'])
    def test_document_and_delete(self, mock_input):
        self.assertTrue(run_cmd([cmds.DOCUMENT[0], 'new thing'], [], [], [], [])[0])
        self.assertTrue(run_cmd([cmds.DELETE[0], 'new thing'], [], [], [], [['new thing', True, 'lorem ipsum']])[0])

if __name__ == "__main__":
    unittest.main()