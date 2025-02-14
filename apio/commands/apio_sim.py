# -*- coding: utf-8 -*-
# -- This file is part of the Apio project
# -- (C) 2016-2024 FPGAwars
# -- Authors
# --  * Jesús Arroyo (2016-2019)
# --  * Juan Gonzalez (obijuan) (2019-2024)
# -- Licence GPLv2
"""Implementation of 'apio sim' command"""

import sys
from pathlib import Path
import click
from apio.managers.scons import SCons
from apio.commands import options
from apio.apio_context import ApioContext, ApioContextScope


# ---------------------------
# -- COMMAND
# ---------------------------

HELP = """
The command ‘apio sim’ simulates a testbench file and displays the simulation
results in a GTKWave graphical window. The testbench is expected to have a
name ending with _tb (e.g., my_module_tb.v).

\b
Example:
  apio sim my_module_tb.v
  apio sim my_module_tb.v --force

[Important] Avoid using the Verilog $dumpfile() function in your testbenches,
as this may override the default name and location Apio sets for the
generated .vcd file.

The sim command defines the INTERACTIVE_SIM macro, which can be used in the
testbench to distinguish between ‘apio test’ and ‘apio sim’. For example,
you can use this macro to ignore certain errors when running with ‘apio sim’
and view the erroneous signals in GTKWave.

For a sample testbench that utilizes this macro, see the example at:
https://github.com/FPGAwars/apio-examples/tree/master/upduino31/testbench

[Hint] When configuring the signals in GTKWave, save the configuration so you
don’t need to repeat it for each simulation.
"""


@click.command(
    name="sim",
    short_help="Simulate a testbench with graphic results.",
    help=HELP,
)
@click.pass_context
@click.argument("testbench", nargs=1, required=True)
@options.force_option_gen(help="Force simulation.")
@options.project_dir_option
def cli(
    _: click.Context,
    # Arguments
    testbench: str,
    # Options
    force: bool,
    project_dir: Path,
):
    """Implements the apio sim command. It simulates a single testbench
    file and shows graphically the signal graphs.
    """

    # -- Create the apio context.
    apio_ctx = ApioContext(
        scope=ApioContextScope.PROJECT_REQUIRED,
        project_dir_arg=project_dir,
    )

    # -- Create the scons manager.
    scons = SCons(apio_ctx)

    # -- Simulate the project with the given parameters
    exit_code = scons.sim({"testbench": testbench, "force_sim": force})

    # -- Done!
    sys.exit(exit_code)
