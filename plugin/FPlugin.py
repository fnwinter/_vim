import os
import vim
import sys
import glob
import hashlib
import platform

CURRENT_WORKING_PATH = vim._getcwd()
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

def get_find_by_extension():
  _os_name == platform.uname().system
  _filter = ""
  if _os_name == 'Linux':
    _filter = ""
  elif _os_name == 'Darwin':
    _filter = ""
  return _filter
