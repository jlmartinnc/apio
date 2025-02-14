## APIO COMMANDS
* [apio](#apio) - Work with FPGAs with ease
  * [apio boards](#apio-boards) - List available board definitions.
  * [apio build](#apio-build) - Synthesize the bitstream.
  * [apio clean](#apio-clean) - Delete the apio generated files.
  * [apio create](#apio-create) - Create an apio.ini project file.
  * [apio drivers](#apio-drivers) - Manage the operating system drivers.
    * [apio drivers ftdi](#apio-drivers-ftdi) - Manage the ftdi drivers.
      * [apio drivers ftdi install](#apio-drivers-ftdi-install) - Install the ftdi drivers.
      * [apio drivers ftdi list](#apio-drivers-ftdi-list) - List the connected ftdi devices.
      * [apio drivers ftdi uninstall](#apio-drivers-ftdi-uninstall) - Uninstall the ftdi drivers.
    * [apio drivers lsusb](#apio-drivers-lsusb) - List connected USB devices.
    * [apio drivers serial](#apio-drivers-serial) - Manage the serial drivers.
      * [apio drivers serial install](#apio-drivers-serial-install) - Install the serial drivers.
      * [apio drivers serial list](#apio-drivers-serial-list) - List the connected serial devices.
      * [apio drivers serial uninstall](#apio-drivers-serial-uninstall) - Uninstall the serial drivers.
  * [apio examples](#apio-examples) - List and fetch apio examples.
    * [apio examples fetch](#apio-examples-fetch) - Fetch the files of an example.
    * [apio examples fetch-board](#apio-examples-fetch-board) - Fetch all examples of a board.
    * [apio examples list](#apio-examples-list) - List the available apio examples.
  * [apio format](#apio-format) - Format verilog source files.
  * [apio fpgas](#apio-fpgas) - List available FPGA definitions.
  * [apio graph](#apio-graph) - Generate a visual graph of the code.
  * [apio lint](#apio-lint) - Lint the verilog code.
  * [apio packages](#apio-packages) - Manage the apio packages.
    * [apio packages fix](#apio-packages-fix) - Fix broken apio packages.
    * [apio packages install](#apio-packages-install) - Install apio packages.
    * [apio packages list](#apio-packages-list) - List apio packages.
    * [apio packages uninstall](#apio-packages-uninstall) - Uninstall apio packages.
  * [apio raw](#apio-raw) - Execute commands directly from the Apio packages.
  * [apio report](#apio-report) - Report design utilization and timing.
  * [apio sim](#apio-sim) - Simulate a testbench with graphic results.
  * [apio system](#apio-system) - Provides system info.
    * [apio system info](#apio-system-info) - Show platform id and other info.
    * [apio system platforms](#apio-system-platforms) - List supported platforms ids.
  * [apio test](#apio-test) - Test all or a single verilog testbench module.
  * [apio upgrade](#apio-upgrade) - Check the latest Apio version.
  * [apio upload](#apio-upload) - Upload the bitstream to the FPGA.

<br>

### apio

```
Usage: apio [OPTIONS] COMMAND [ARGS]...

  Work with FPGAs with ease.

  Apio is an easy to use and open-source command-line suite designed to
  streamline FPGA programming. It supports a wide range of tasks, including
  linting, building, simulation, unit testing, and programming FPGA boards.

  An Apio project consists of a directory containing a configuration file
  named 'apio.ini', along with FPGA source files, testbenches, and pin
  definition files.

  Apio commands are intuitive and perform their intended functionalities right
  out of the box. For example, the command apio upload automatically compiles
  the design in the current directory and uploads it to the FPGA board.

  For detailed information about any Apio command, append the -h flag to view
  its help text. For instance:

  apio build -h
  apio drivers ftdi install -h

  For more information about the Apio project, visit the official Apio Wiki
  https://github.com/FPGAwars/apio/wiki/Apio

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Build commands:
  apio build     Synthesize the bitstream.
  apio upload    Upload the bitstream to the FPGA.
  apio clean     Delete the apio generated files.

Verification commands:
  apio lint      Lint the verilog code.
  apio format    Format verilog source files.
  apio sim       Simulate a testbench with graphic results.
  apio test      Test all or a single verilog testbench module.
  apio report    Report design utilization and timing.
  apio graph     Generate a visual graph of the code.

Setup commands:
  apio create    Create an apio.ini project file.
  apio packages  Manage the apio packages.
  apio drivers   Manage the operating system drivers.

Utility commands:
  apio boards    List available board definitions.
  apio fpgas     List available FPGA definitions.
  apio examples  List and fetch apio examples.
  apio system    Provides system info.
  apio raw       Execute commands directly from the Apio packages.
  apio upgrade   Check the latest Apio version.

```

<br>

### apio boards

```
Usage: apio boards [OPTIONS]

  The command 'apio boards' lists the FPGA boards recognized by Apio. Custom
  boards can be defined by placing a custom 'boards.json' file in the project
  directory, which will override Apio’s default 'boards.json' file.

  Examples:
    apio boards                # List all boards
    apio boards | grep ecp5    # Filter boards results
    apio boards --project-dir foo/bar  # Use a different

Options:
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio build

```
Usage: apio build [OPTIONS]

  The command 'apio build' processes the project’s source files and generates
  a bitstream file, which can then be uploaded to your FPGA.

  The 'apio build' command compiles all .v files (e.g., my_module.v) in the
  project directory, except those whose names end with _tb (e.g.,
  my_module_tb.v), as these are assumed to be testbenches.

  Examples:
    apio build       # Build
    apio build -v    # Build with verbose info

Options:
  -p, --project-dir path  Set the root directory for the project.
  -v, --verbose           Show detailed output.
  --verbose-yosys         Show detailed yosys output.
  --verbose-pnr           Show detailed pnr output.
  -h, --help              Show this message and exit.
```

<br>

### apio clean

```
Usage: apio clean [OPTIONS]

  The command 'apio clean' removes temporary files generated in the project
  directory by previous Apio commands.

  Example:
    apio clean

Options:
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio create

```
Usage: apio create [OPTIONS]

  The command 'apio create' creates a new `apio.ini` project file and is
  typically used when setting up a new Apio project.

  Examples:
    apio create --board alhambra-ii
    apio create --board alhambra-ii --top-module MyModule

  [Note] This command only creates a new 'apio.ini' file, rather than a
  complete and buildable project. To create complete projects, refer to the
  'apio examples' command.

Options:
  -b, --board board_id    Set the board.  [required]
  -t, --top-module name   Set the top level module name.
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio drivers

```
Usage: apio drivers [OPTIONS] COMMAND [ARGS]...

  The command group ‘apio drivers’ contains subcommands used to manage the
  drivers on your system.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio drivers ftdi    Manage the ftdi drivers.
  apio drivers serial  Manage the serial drivers.
  apio drivers lsusb   List connected USB devices.

```

<br>

### apio drivers ftdi

```
Usage: apio drivers ftdi [OPTIONS] COMMAND [ARGS]...

  The command group 'apio drivers ftdi' includes subcommands that help manage
  the FTDI drivers on your system.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio drivers ftdi install    Install the ftdi drivers.
  apio drivers ftdi uninstall  Uninstall the ftdi drivers.
  apio drivers ftdi list       List the connected ftdi devices.

```

<br>

### apio drivers ftdi install

```
Usage: apio drivers ftdi install [OPTIONS]

  The command 'apio drivers ftdi install' installs on your system the FTDI
  drivers required by some FPGA boards.

  Examples:
    apio drivers ftdi install      # Install the ftdi drivers.
    apio drivers ftdi uinstall     # Uinstall the ftdi drivers.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers ftdi list

```
Usage: apio drivers ftdi list [OPTIONS]

  The command 'apio drivers ftdi list' displays the FTDI devices currently
  connected to your computer. It is useful for diagnosing FPGA board
  connectivity issues.

  Examples:
    apio drivers ftdi list     # List the ftdi devices.

  [Hint] This command uses the lsftdi utility, which can also be invoked
  directly with the 'apio raw -- lsftdi <flags>' command.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers ftdi uninstall

```
Usage: apio drivers ftdi uninstall [OPTIONS]

  The command 'apio drivers ftdi uninstall' removes the FTDI drivers that may
  have been installed earlier.

  Examples:
    apio drivers ftdi install      # Install the ftdi drivers.
    apio drivers ftdi uinstall     # Uinstall the ftdi drivers.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers lsusb

```
Usage: apio drivers lsusb [OPTIONS]

  The command ‘apio drivers lsusb’ runs the lsusb utility to list the USB
  devices connected to your computer. It is typically used for diagnosing
  connectivity issues with FPGA boards.

  Examples:
    apio drivers lsusb      # List the usb devices

  [Hint] You can also run the lsusb utility using the command 'apio raw --
  lsusb <flags>'.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers serial

```
Usage: apio drivers serial [OPTIONS] COMMAND [ARGS]...

  The command group 'apio drivers serial' includes subcommands designed to
  manage and configure the serial drivers on your system.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio drivers serial install    Install the serial drivers.
  apio drivers serial uninstall  Uninstall the serial drivers.
  apio drivers serial list       List the connected serial devices.

```

<br>

### apio drivers serial install

```
Usage: apio drivers serial install [OPTIONS]

  The command ‘apio drivers serial install’ installs the necessary serial
  drivers on your system, as required by certain FPGA boards.

  Examples:
    apio drivers serial install      # Install the ftdi drivers.
    apio drivers serial uinstall     # Uinstall the ftdi drivers.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers serial list

```
Usage: apio drivers serial list [OPTIONS]

  The command ‘apio drivers serial list’ lists the serial devices connected to
  your computer. It is useful for diagnosing FPGA board connectivity issues.

  Examples:
    apio drivers serial list     # List the serial devices.

  [Hint] This command executes the utility lsserial, which can also be invoked
  using the command 'apio raw -- lsserial <flags>'.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio drivers serial uninstall

```
Usage: apio drivers serial uninstall [OPTIONS]

  The command ‘apio drivers serial uninstall’ removes the serial drivers that
  you may have installed earlier.

  Examples:
    apio drivers serial install      # Install the serial drivers.
    apio drivers serial uinstall     # Uinstall the serial drivers.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio examples

```
Usage: apio examples [OPTIONS] COMMAND [ARGS]...

  The command group ‘apio examples’ provides subcommands for listing and
  fetching Apio-provided examples. Each example is a self-contained mini-
  project that can be built and uploaded to an FPGA board.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio examples list         List the available apio examples.
  apio examples fetch        Fetch the files of an example.
  apio examples fetch-board  Fetch all examples of a board.

```

<br>

### apio examples fetch

```
Usage: apio examples fetch [OPTIONS] EXAMPLE

  The command ‘apio examples fetch’ fetches the files of the specified example
  to the current directory or to the directory specified by the –dst option.
  The destination directory does not need to exist, but if it does, it must be
  empty.

  Examples:
    apio examples fetch alhambra-ii/ledon
    apio examples fetch alhambra-ii/ledon -d foo/bar

  [Hint] For the list of available examples, type ‘apio examples list’.

Options:
  -d, --dst path  Set a different destination directory.
  -h, --help      Show this message and exit.
```

<br>

### apio examples fetch-board

```
Usage: apio examples fetch-board [OPTIONS] BOARD

  The command ‘apio examples fetch-board’ is used to fetch all the Apio
  examples for a specific board. The examples are copied to the current
  directory or to the specified destination directory if the –dst option is
  provided.

  Examples:
    apio examples fetch-board alhambra-ii             # Fetch to local directory
    apio examples fetch-board alhambra-ii -d foo/bar  # Fetch to foo/bar

  [Hint] For the list of available examples, type ‘apio examples list’.

Options:
  -d, --dst path  Set a different destination directory.
  -h, --help      Show this message and exit.
```

<br>

### apio examples list

```
Usage: apio examples list [OPTIONS]

  The command ‘apio examples list’ lists the available Apio project examples
  that you can use.

  Examples:
    apio examples list                     # List all examples
    apio examples list | grep alhambra-ii  # Show examples of a specific board.
    apio examples list | grep -i blink     # Show all blinking examples.



Options:
  -h, --help  Show this message and exit.
```

<br>

### apio format

```
Usage: apio format [OPTIONS] [FILES]...

  The command ‘apio format’ formats Verilog source files to ensure consistency
  and style without altering their semantics. The command accepts the names of
  pecific source files to format or formats all project source files by
  default.

  Examples:
    apio format                    # Format all source files.
    apio format -v                 # Same as above but with verbose output.
    apio format main.v main_tb.v   # Format the two tiven files.

  The format command utilizes the format tool from the Verible project, which
  can be configured by setting its flags in the apio.ini project file For
  example:

  format-verible-options =
      --column_limit=80
      --indentation_spaces=4

  If needed, sections of source code can be protected from formatting using
  Verible formatter directives:

  // verilog_format: off
  ... untouched code ...
  // verilog_format: on

  For a full list of Verible formatter flags, refer to the documentation page
  online or use the command 'apio raw -- verible-verilog-format --helpful'.

Options:
  -p, --project-dir path  Set the root directory for the project.
  -v, --verbose           Show detailed output.
  -h, --help              Show this message and exit.
```

<br>

### apio fpgas

```
Usage: apio fpgas [OPTIONS]

  The command ‘apio fpgas’ lists the FPGAs recognized by Apio. Custom FPGAs
  supported by the underlying Yosys toolchain can be defined by placing a
  custom fpgas.json file in the project directory, overriding Apio’s standard
  fpgas.json file.

  Examples:
    apio fpgas               # List all fpgas
    apio fpgas | grep gowin  # Filter FPGA results.

Options:
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio graph

```
Usage: apio graph [OPTIONS]

  The command ‘apio graph’ generates a graphical representation of the Verilog
  code in the project.

  Examples:
    apio graph               # Generate a svg file.
    apio graph --pdf         # Generate a pdf file.
    apio graph --png         # Generate a png file.
    apio graph -t my_module  # Graph my_module module.

  [Hint] On Windows, type ‘explorer _build/hardware.svg’ to view the graph,
  and on Mac OS type ‘open _build/hardware.svg’.

Options:
  --pdf                   Generate a pdf file.
  --png                   Generate a png file.
  -p, --project-dir path  Set the root directory for the project.
  -t, --top-module name   Set the name of the top module to graph.
  -v, --verbose           Show detailed output.
  -h, --help              Show this message and exit.
```

<br>

### apio lint

```
Usage: apio lint [OPTIONS]

  The command ‘apio lint’ scans the project’s Verilog code and reports errors,
  inconsistencies, and style violations. The command uses the Verilator tool,
  which is included in the standard Apio installation.

  Examples:
    apio lint
    apio lint -t my_module
    apio lint --all

Options:
  -t, --top-module name   Restrict linting to this module and its depedencies.
  -a, --all               Enable all warnings, including code style warnings.
  --nostyle               Disable all style warnings.
  --nowarn nowarn         Disable specific warning(s).
  --warn warn             Enable specific warning(s).
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio packages

```
Usage: apio packages [OPTIONS] COMMAND [ARGS]...

  The command group ‘apio packages’ provides commands to manage the
  installation of Apio packages. These are not Python packages but Apio-
  specific packages containing various tools and data essential for the
  operation of Apio. These packages are installed after the installation of
  the Apio Python package itself, using the command ‘apio packages install’.

  The list of available packages depends on the operating system you are using
  and may vary between different operating systems.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio packages install    Install apio packages.
  apio packages uninstall  Uninstall apio packages.
  apio packages list       List apio packages.
  apio packages fix        Fix broken apio packages.

```

<br>

### apio packages fix

```
Usage: apio packages fix [OPTIONS]

  The command ‘apio packages fix’ resolves partially installed or leftover
  Apio packages that are listed as broken by the command ‘apio packages list’.
  If there are no broken packages, the command does nothing and exits.

  Examples:
    apio packages fix           # Fix package errors.
    apio packages fix  -v       # Same but with verbose output.

Options:
  -v, --verbose  Show detailed output.
  -h, --help     Show this message and exit.
```

<br>

### apio packages install

```
Usage: apio packages install [OPTIONS] [PACKAGES]...

  The command ‘apio packages install’ installs Apio packages that are required
  for the operation of Apio on your system.

  Examples:
    apio packages install                   # Install all missing packages.
    apio packages install --force           # Re/install all missing packages.
    apio packages install oss-cad-suite     # Install just this package.
    apio packages install examples@0.0.32   # Install a specific version.

  Adding the --force option forces the reinstallation of existing packages;
  otherwise, packages that are already installed correctly remain unchanged.

Options:
  -f, --force    Force installation.
  -v, --verbose  Show detailed output.
  -h, --help     Show this message and exit.
```

<br>

### apio packages list

```
Usage: apio packages list [OPTIONS]

  The command ‘apio packages list’ lists the available and installed Apio
  packages. The list of available packages depends on the operating system you
  are using and may vary between operating systems.

  Examples:
    apio packages list

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio packages uninstall

```
Usage: apio packages uninstall [OPTIONS] [PACKAGES]...

  The command ‘apio packages uninstall’ removes installed Apio packages from
  your system. The command does not uninstall the Apio tool itself.

  Examples:
    apio packages uninstall                 # Uninstall all packages.
    apio packages uninstall --sayyes        # Same but does not ask yes/no.
    apio packages uninstall oss-cad-suite   # Uninstall only given package(s).

Options:
  -y, --sayyes   Automatically answer YES to all the questions.
  -v, --verbose  Show detailed output.
  -h, --help     Show this message and exit.
```

<br>

### apio raw

```
Usage: apio raw [OPTIONS] COMMAND

  The command ‘apio raw’ allows you to bypass Apio and run underlying tools
  directly. This is an advanced command that requires familiarity with the
  underlying tools.

  Before running the command, Apio temporarily modifies system environment
  variables such as $PATH to provide access to its packages. To view these
  environment changes, run the command `apio raw --env`.

  Examples:
    apio raw -- yosys --version           # Yosys version
    apio raw -v -- yosys --version        # Same but with verbose apio info.
    apio raw -- yosys                     # Run Yosys in interactive mode.
    apio raw -- icepll -i 12 -o 30        # Calc ICE PLL
    apio raw --env                        # Show apio env setting.
    apio raw -h                           # Print this help info.

  The -- token is used to separate Apio commands and their arguments from the
  underlying tools and their arguments. It can be omitted in some cases, but
  it’s a good practice to always use it. As a rule of thumb, always prefix the
  raw command you want to run with 'apio raw -- '.

Options:
  -e, --env      Show the apio env changes.
  -v, --verbose  Show detailed output.
  -h, --help     Show this message and exit.
```

<br>

### apio report

```
Usage: apio report [OPTIONS]

  The command ‘apio report’ provides information on the utilization and timing
  of the design. It is useful for analyzing utilization bottlenecks and
  verifying that the design can operate at the desired clock speed.

  Examples:
    apio report
    epio report --verbose

Options:
  -p, --project-dir path  Set the root directory for the project.
  -v, --verbose           Show detailed output.
  -h, --help              Show this message and exit.
```

<br>

### apio sim

```
Usage: apio sim [OPTIONS] TESTBENCH

  The command ‘apio sim’ simulates a testbench file and displays the
  simulation results in a GTKWave graphical window. The testbench is expected
  to have a name ending with _tb (e.g., my_module_tb.v).

  Example:
    apio sim my_module_tb.v
    apio sim my_module_tb.v --force

  [Important] Avoid using the Verilog $dumpfile() function in your
  testbenches, as this may override the default name and location Apio sets
  for the generated .vcd file.

  The sim command defines the INTERACTIVE_SIM macro, which can be used in the
  testbench to distinguish between ‘apio test’ and ‘apio sim’. For example,
  you can use this macro to ignore certain errors when running with ‘apio sim’
  and view the erroneous signals in GTKWave.

  For a sample testbench that utilizes this macro, see the example at:
  https://github.com/FPGAwars/apio-examples/tree/master/upduino31/testbench

  [Hint] When configuring the signals in GTKWave, save the configuration so
  you don’t need to repeat it for each simulation.

Options:
  -f, --force             Force simulation.
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio system

```
Usage: apio system [OPTIONS] COMMAND [ARGS]...

  The command group ‘apio system’ contains subcommands that provide
  information about the system and Apio’s installation.

Options:
  -h, --help  Show this message and exit.

Subcommands:
  apio system platforms  List supported platforms ids.
  apio system info       Show platform id and other info.

```

<br>

### apio system info

```
Usage: apio system info [OPTIONS]

  The command ‘apio system info’ provides general information about your
  system and Apio installation, which is useful for diagnosing Apio
  installation issues.

  Examples:
    apio system info       # Show platform id and info.

  [Advanced] The default location of the Apio home directory, where
  preferences and packages are stored, is in the .apio directory under the
  user’s home directory. This location can be changed using the APIO_HOME
  environment variable.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio system platforms

```
Usage: apio system platforms [OPTIONS]

  The command ‘apio system platforms’ lists the platform IDs supported by
  Apio, with the effective platform ID of your system highlighted.

  Examples:
    apio system platforms   # List supported platform ids.

  [Advanced] The automatic platform ID detection of Apio can be overridden by
  defining a different platform ID using the APIO_PLATFORM environment
  variable.

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio test

```
Usage: apio test [OPTIONS] [TESTBENCH_FILE]

  The command ‘apio test’ simulates one or all the testbenches in the project
  and is useful for automated testing of your design. Testbenches are expected
  to have names ending with _tb (e.g., my_module_tb.v) and should exit with
  the $fatal directive if an error is detected.

  Examples
    apio test                 # Run all *_tb.v testbenches.
    apio test my_module_tb.v  # Run a single testbench

  [Important] Avoid using the Verilog $dumpfile() function in your
  testbenches, as this may override the default name and location Apio sets
  for the generated .vcd file.

  For a sample testbench compatible with Apio features, see:
  https://github.com/FPGAwars/apio-examples/tree/master/upduino31/testbench

  [Hint] To simulate a testbench with a graphical visualization of the
  signals, refer to the ‘apio sim’ command.

Options:
  -p, --project-dir path  Set the root directory for the project.
  -h, --help              Show this message and exit.
```

<br>

### apio upgrade

```
Usage: apio upgrade [OPTIONS]

  The command ‘apio upgrade’ checks for the version of the latest Apio release
  and provides upgrade directions if necessary.

  Examples:
    apio upgrade

Options:
  -h, --help  Show this message and exit.
```

<br>

### apio upload

```
Usage: apio upload [OPTIONS]

  The command ‘apio upload’ builds the bitstream file (similar to the apio
  build command) and uploads it to the FPGA board.

  Examples:
    apio upload

Options:
  --serial-port serial-port  Set the serial port.
  --ftdi-id ftdi-id          Set the FTDI id.
  -s, --sram                 Perform SRAM programming.
  -f, --flash                Perform FLASH programming.
  -v, --verbose              Show detailed output.
  --verbose-yosys            Show detailed yosys output.
  --verbose-pnr              Show detailed pnr output.
  -p, --project-dir path     Set the root directory for the project.
  -h, --help                 Show this message and exit.
```
