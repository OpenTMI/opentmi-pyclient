import sys
import unittest
from mock import MagicMock, patch, call, Mock
from opentmi_client.cli.main import opentmiclient_main, OpentTMIClientCLI


class TestCli(unittest.TestCase):
    @patch('sys.stdout', new_callable=Mock())
    @patch("sys.exit")
    def test_help(self, mock_exit, mock_stdout):
        fake_args = ["opentmi", "--help"]
        with patch('sys.argv', fake_args):
            opentmiclient_main()
        mock_exit.assert_called_with(0)

    @patch('sys.stdout', new_callable=Mock())
    @patch("sys.exit")
    def test_version(self, mock_exit, mock_stdout):
        fake_args = ["opentmi", "version"]
        with patch('sys.argv', fake_args):
            opentmiclient_main()
        mock_exit.assert_called_with(0)
