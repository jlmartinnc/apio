"""A python script to print the -h help of all apio commands."""

import os
from typing import List, Self
from dataclasses import dataclass
import click
from apio.commands.apio import cli as root

@dataclass(frozen=True)
class CmdInfo:
    """Represents the information of a single apio command."""
    name: str
    path: List[str]
    cli: click.Command
    children: List[Self]


def scan_children(cmd_info:CmdInfo, cmd_list:List[CmdInfo]):
    """Fill in recursivly the childrens of cmd_info and collect all the 
    commands encountered in cmd_list."""
    assert isinstance(cmd_info, CmdInfo)
    if hasattr(cmd_info.cli, 'commands'):
        for child_name, child_cli in cmd_info.cli.commands.items():
            child_info = CmdInfo(child_name, cmd_info.path + [child_name], child_cli, [])
            cmd_info.children.append(child_info)
            cmd_list.append(child_info)
            scan_children(child_info, cmd_list)

def get_cmds_infos() -> List[CmdInfo]:
   """Construt a list with the CmdInfo of all apio commands."""
   root_info = CmdInfo("apio", ["apio"], root, [])
   cmd_list = [root_info]
   scan_children(root_info, cmd_list)
   return cmd_list

# -- Get the commands list.
cmds_infos = get_cmds_infos()

cmds_infos.sort(key=lambda x: x.path)

# -- Dump the commands -h help text.
for cmd_info in cmds_infos:
    cmd_path = ' '.join(cmd_info.path)
    click.secho("\n<br><br>\n")
    click.secho(f"### {cmd_path.upper()}", fg="magenta")
    click.secho()

    help_command = f"{cmd_path} -h"
    click.secho('```')
    exit_code = os.system(help_command)
    assert exit_code == 0
    click.secho('```')



