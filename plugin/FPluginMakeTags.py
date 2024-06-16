import vim
import os
import sys
import inspect

MODULE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(MODULE_PATH)

from FPlugin import create_tag_save_path
from FPlugin import get_git_path
from FPlugin import get_hash_path

# create root tag path
tag_save_path = create_tag_save_path()

# create tag path
git_root_path = get_git_path()
tag_path = get_hash_path(tag_save_path, git_root_path)

print("git path [%s] : tag path [%s]" % (git_root_path, tag_path))

# Push working path
OLD_WORKING_PATH = os.getcwd()
os.chdir(tag_path)

if os.path.exists(tag_path):
  # Make ctag list
  ctag_ext_list = " -regex '.*\.\(java\|kt\|h\|hpp\|cpp\|c\|s\|S\|in\|py\|lua\)$' "
  #ctag_ext_list = " \( -iname '*.h' -o -name '*.cpp' -o -iname '*.java' \) "
  cmd = "time find " + git_root_path + " -type f  " + ctag_ext_list + " -exec ctags -R {} +"
  print(cmd)
  os.system(cmd)

  # Make cscope list
  cmd = "time find " + git_root_path + " -type f " + ctag_ext_list + " -print > cscope.files "
  print(cmd)
  os.system(cmd)
  cmd = "time cscope -i cscope.files -b"
  print(cmd)
  os.system(cmd)

# Pop working path
os.chdir(OLD_WORKING_PATH)
