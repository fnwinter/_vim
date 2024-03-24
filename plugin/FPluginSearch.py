import vim
import subprocess

def Search():
  current_working_path = vim._getcwd()
  vim.command('let file_name = input("search file ?> ")')
  file_name = vim.eval("file_name")
  if file_name.strip() == "":
    return

  print("\r\n-Result-")
  result = subprocess.check_output(["git" , "ls-files", file_name])
  str_result = result.decode("utf-8")

  index = 0
  files = str_result.split('\n')
  for file_ in files:
      if not file_.strip(): continue
      print("[%d] : %s" % (index, file_))
      index = index + 1

  vim.command('let file_index = input("file index ?> ")')
  file_index = vim.eval("file_index")
  if file_index.strip() != "" and int(file_index) < len(files) and len(files) != 0:
    print("open the file : %s" % files[int(file_index)])
    vim.command("open %s" % files[int(file_index)])

Search()
