"""
  Test for the "apio lint" command
"""

from test.conftest import ApioRunner
from apio.commands.apio import cli as apio


def test_lint_no_packages(apio_runner: ApioRunner):
    """Test: apio lint with missing packages."""

    with apio_runner.in_sandbox() as sb:

        # -- Create apio.ini file.
        sb.write_default_apio_ini()

        # -- Execute "apio lint"
        result = sb.invoke_apio_cmd(apio, ["lint"])
        assert result.exit_code == 1, result.output
        assert "package 'oss-cad-suite' is not installed" in result.output
