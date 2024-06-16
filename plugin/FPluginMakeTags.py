import vim
import os
import sys
import inspect

MODULE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(MODULE_PATH)

from FPlugin import create_tag_save_path
from FPlugin import get_git_path
from FPlugin import get_hash_path
from FPlugin import get_find_filter

# create root tag path
tag_save_path = create_tag_save_path()

# create tag path
git_root_path = get_git_path()
tag_path = get_hash_path(tag_save_path, git_root_path)

print(f"git path {git_root_path}] : tag path [{tag_path}]")

# Push working path
OLD_WORKING_PATH = os.getcwd()
os.chdir(tag_path)

if os.path.exists(tag_path):
  # Make ctag list
  ctag_ext_list = get_find_filter()
  cmd = f"time find {git_root_path} -type f {ctag_ext_list} -exec ctags -R {{}} + "
  print(cmd)
  os.system(cmd)

  # Make cscope list
  cmd = f"time find {git_root_path} -type f {ctag_ext_list} -print > cscope.files"
  print(cmd)
  os.system(cmd)
  cmd = "time cscope -i cscope.files -b"
  print(cmd)
  os.system(cmd)

# Pop working path
os.chdir(OLD_WORKING_PATH)
