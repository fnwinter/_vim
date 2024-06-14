import vim
import subprocess
import shutil
import os
import glob
import hashlib
import sys

CURRENT_WORKING_PATH = vim._getcwd()
USER_HOME = os.path.expanduser("~")
TAG_SAVE_PATH = os.path.join(USER_HOME,".fplugin_tag")
os.system("mkdir -p %s" % TAG_SAVE_PATH)

GIT_ROOT_PATH = None
depth = 0
max_depth = 50
depth_path = ""
while True:
  found = glob.glob(os.path.join(CURRENT_WORKING_PATH, depth_path, ".git"))
  if found:
    GIT_ROOT_PATH = os.path.join(CURRENT_WORKING_PATH, depth_path)
    break
  depth_path = depth_path + os.path.pardir
  depth = depth + 1
  if depth == max_depth:
    break

if not GIT_ROOT_PATH:
  GIT_ROOT_PATH = CURRENT_WORKING_PATH

GIT_ABS_PATH = os.path.abspath(GIT_ROOT_PATH)
hash_tag_path_name = hashlib.sha224(str.encode(GIT_ABS_PATH)).hexdigest()
TAG_PATH = os.path.join(TAG_SAVE_PATH, hash_tag_path_name[:16])
print("git path [%s] : tag path [%s]" % (GIT_ABS_PATH, TAG_PATH))

OLD_WORKING_PATH = os.getcwd()
os.chdir(TAG_PATH)
# Load tags
vim.command("cs add %s/cscope.out" % TAG_PATH)
vim.command("set tags=%s/tags" % TAG_PATH)

os.chdir(OLD_WORKING_PATH)
print("Tag loaded")
