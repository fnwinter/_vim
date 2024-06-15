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
git_root_path = get_git_path()
tag_path = get_hash_path(tag_save_path, git_root_path)

# Load tags
print(tag_path)
vim.command("cs add %s/cscope.out" % tag_path)
vim.command("set tags=%s/tags" % tag_path)

print("Tag loaded")
