# vim
:PluginInstall

https://ctags.sourceforge.net/

sudo apt-get -y install exuberant-ctags

https://cscope.sourceforge.net/

sudo apt-get -y install cscope

# For mac

git clone https://github.com/vim/vim.git

cd vim/src

./configure --with-features=huge --enable-python3interp --enable-cscope

make

sudo make install

in vim, set csprg=/usr/bin/cscope

