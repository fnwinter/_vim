function! FPlugin#git_search()
  exec 'py3file ~/.vim/plugin/FPluginSearch.py'
endfunction

function! FPlugin#make_tags(...)
  exec 'py3file ~/.vim/plugin/FPluginMakeTags.py'
endfunction

function! FPlugin#load_tags(...)
  exec 'py3file ~/.vim/plugin/FPluginLoadTags.py'
endfunction

function! FPlugin#search_tags()
  let input = input("keyword ?> ")
  if input != ""
    execute "cs find e ".input
  endif
endfunction

function! FPlugin#terminal()
  exec 'py3file ~/.vim/plugin/FPluginTerminal.py'
endfunction

command Search call FPlugin#git_search()
command -nargs=* MakeTag call FPlugin#make_tags(<f-args>)
command -nargs=* LoadTag call FPlugin#load_tags(<f-args>)
command SearchTag call FPlugin#search_tags()
command Terminal call FPlugin#terminal()
