
import unittest
import subprocess
from unittest.mock import patch, MagicMock
from dotnet_pilot.commands import run_command

class TestCommands(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_run_command_success(self, mock_popen):
        # Arrange
        mock_process = MagicMock()
        mock_process.communicate.return_value = ('Success', '')
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        append_output_func = MagicMock()

        # Act
        run_command('dotnet --version', '.', append_output_func)

        # Assert
        mock_popen.assert_called_with(
            'dotnet --version',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd='.',
            bufsize=1,
            universal_newlines=True
        )
        self.assertEqual(append_output_func.call_count, 3)

    def test_run_command_empty_command(self):
        # Test with empty command
        with patch('tkinter.messagebox.showwarning') as mock_warning:
            append_output_func = MagicMock()
            run_command('', '.', append_output_func)
            mock_warning.assert_called_with("Warning", "Please enter a command or fill required fields.")

    def test_run_command_empty_directory(self):
        # Test with empty working directory
        with patch('tkinter.messagebox.showwarning') as mock_warning:
            append_output_func = MagicMock()
            run_command('dotnet --version', '', append_output_func)
            mock_warning.assert_called_with("Warning", "Working directory is required.")

if __name__ == '__main__':
    unittest.main()
