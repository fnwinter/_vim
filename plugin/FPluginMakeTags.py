import vim
import subprocess
import shutil
import os
import glob
import hashlib
import sys

# create root tag path
CURRENT_WORKING_PATH = vim._getcwd()
USER_HOME = os.path.expanduser("~")
TAG_SAVE_PATH = os.path.join(USER_HOME,".fplugin_tag")
os.system("mkdir -p %s" % TAG_SAVE_PATH)

# find git root path
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

# create tag path
GIT_ABS_PATH = os.path.abspath(GIT_ROOT_PATH)
hash_tag_path_name = hashlib.sha224(str.encode(GIT_ABS_PATH)).hexdigest()
TAG_PATH = os.path.join(TAG_SAVE_PATH, hash_tag_path_name[:16])
os.system("mkdir -p %s" % TAG_PATH)
print("git path [%s] : tag path [%s]" % (GIT_ABS_PATH, TAG_PATH))

# Push working path
OLD_WORKING_PATH = os.getcwd()
os.chdir(TAG_PATH)

# Make ctag list
ctag_ext_list = " '.*\\.\\(java\\|hpp\\|h\\|cc\\|cpp\\|c\\|s\\|S\\|in\\|py\\|lua\\)' " 
cmd = "time find " + GIT_ABS_PATH + " -regex " + ctag_ext_list + " -exec ctags -R {} +"
os.system(cmd)

# Make cscope list
cmd = "time find " + GIT_ABS_PATH + ctag_ext_list + " -type f -print > cscope.files "
os.system(cmd)
cmd = "time cscope -i cscope.files -b"
os.system(cmd)

# Pop working path
os.chdir(OLD_WORKING_PATH)
