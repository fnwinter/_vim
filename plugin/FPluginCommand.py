import vim
import subprocess
import shutil
import os
import glob
import hashlib
import sys
import inspect

sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from FPlugin import create_tag_save_path
from FPlugin import get_git_path
from FPlugin import get_hash_path

tag_save_path = create_tag_save_path()

_command = ""
try:
  _command = vim.eval('a:1')
except:
  pass

command_file = os.path.join(tag_save_path, "command.txt")
if _command.lower() == "show" and os.path.exists(command_file):
  with open(command_file) as f:
    print("=== command ===")
    lines = f.readlines()
    for _index in range(len(lines)):
      print(f"[{_index}] {lines[_index]}")
    
    vim.command('let command = input("command ?> ")')
    c = vim.eval("command")
    if c.strip() != "":
      _c = int(c)
      vim.command(f"!{lines[_c]}")

