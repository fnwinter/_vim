def fplugin_create_root_path():
  CURRENT_WORKING_PATH = vim._getcwd()
  USER_HOME = os.path.expanduser("~")
  TAG_SAVE_PATH = os.path.join(USER_HOME,".fplugin_tag")
  os.system("mkdir -p %s" % TAG_SAVE_PATH)
