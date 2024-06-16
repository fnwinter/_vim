import os
import sys
import glob
import hashlib
import platform

try:
  import vim
  CURRENT_WORKING_PATH = vim._getcwd()
except:
  pass

USER_HOME = os.path.expanduser("~")

def create_tag_save_path():
  _tag_save_path = os.path.join(USER_HOME,".fplugin_tag")
  os.system("mkdir -p %s" % _tag_save_path)
  return _tag_save_path

def get_git_path():
  _git_path = None
  depth = 0
  max_depth = 50
  depth_path = ""
  while True:
    found = glob.glob(os.path.join(CURRENT_WORKING_PATH, depth_path, ".git"))
    if found:
      _git_path = os.path.join(CURRENT_WORKING_PATH, depth_path)
      break
    depth_path = depth_path + os.path.pardir
    depth = depth + 1
    if depth == max_depth:
      break

  if not _git_path:
    _git_path = CURRENT_WORKING_PATH
  return os.path.abspath(_git_path)

def get_hash_path(tag_path, git_path):
  hash_tag_path_name = hashlib.sha224(str.encode(git_path)).hexdigest()
  _tag_path = os.path.join(tag_path, hash_tag_path_name[:16])
  os.system("mkdir -p %s" % _tag_path)
  return _tag_path

def get_find_filter():
  """
  >>> print(get_find_filter())
  \( -iname '*.h'  -o  -iname '*.hpp'  -o  -iname '*.c'  -o  -iname '*.cpp'  -o  -iname '*.cxx'  -o  -iname '*.py'  -o  -iname '*.lua'  -o  -iname '*.java'  -o  -iname '*.kt'  -o  -iname '*.rs'  -o  -iname '*.cs'  -o  -iname '*.in'  -o  -iname '*.s'  -o  -iname '*.S' \)
  """

  _filter = "\("
  ext_list = ['h', 'hpp', 'c', 'cpp', 'cxx', 'py','lua','java','kt','rs','cs', 'in', 's', 'S']
  for ext in ext_list:
    _filter += f" -iname '*.{ext}' "
    if ext != ext_list[-1]:
      _filter += ' -o '
  _filter += "\)"
  return _filter
