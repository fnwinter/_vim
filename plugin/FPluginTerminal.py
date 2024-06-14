import subprocess
import vim

current_working_path = vim._getcwd()

while True:
  vim.command('let command = input("%s $ ")' % current_working_path)
  command = vim.eval("command")
  if command == 'exit' or command == '':
    break
  output = subprocess.check_output(command.strip().split(' '), shell=True, timeout=10)
  str_output = output.decode('utf-8')
  print(str_output + "\n")

