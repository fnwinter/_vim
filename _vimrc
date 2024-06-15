set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
set rtp+=~/.vim/
call vundle#begin()

"--- Custom vundle settings START
Plugin 'The-NERD-tree'
"--- Custom vundle settings END

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"--- Basic vim settings ---
set nu 
set guifont=Liberation\Mono
set shiftwidth=2
set tabstop=2
set softtabstop=2
set expandtab
set ff=unix
set nobackup
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [ASCII=\%03.3b]\ [HEX=\%02.2B]\ [POS=%04l,%04v][%p%%]\ [LEN=%L]
set laststatus=2
set autoindent
set smartindent
set hlsearch
set guioptions+=m
set clipboard=unnamedplus
set noswapfile
colorscheme desert
let NERDTreeShowHidden=1

"--- Auto commands setting ---
autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd w
autocmd VimEnter * silent execute "!~/.vim/cp_rc.sh"
autocmd FileType python setl sw=2 sts=2 et

"---------------------- Cscope settings ---------------------------------------
set csprg=/usr/bin/cscope
set csto=0
set cst
set nocsverb
set cscopequickfix=s-,c-,d-,i-,t-,e-,f-
set csverb

"=-= Key mappings =-=
map <C-w>         :wincmd w<CR>
map <C-n>         :NERDTree<CR>
map <C-g>         :NERDTreeFind<CR>
map <C-b>         :marks<CR>
map <C-x>         :vne<CR>
map <C-o>         :vertical res -5<CR>
map <C-p>         :vertical res +5<CR>

map <C-s>         :Search<CR>
map <C-l>         :LoadTag<CR>
map <C-0>         :SearchTag<CR>
map <C-t>         :Terminal<CR>

map <C-e>         :call OpenExplore()<CR>
map <C-S-h>       :call Help()<CR>
map <C-S-r>       :redraw!<CR>

"=-= Functions =-=
function OpenExplore()
  execute "Explore"
endfunction

function Help()
  echo "=== Help ==="
  echo "Search -> search file"
  echo "LoadTag -> load ctags"
  echo "MakeTag -> make ctags and cscope"
  echo "Terminal -> call terminal"
endfunction
