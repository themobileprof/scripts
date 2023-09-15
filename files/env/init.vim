" ~/.config/nvim/init.vim 
call plug#begin('~/.local/share/nvim/plugged')
	Plug 'preservim/nerdtree'
	Plug 'mattn/emmet-vim'
	Plug 'junegunn/fzf'
	Plug 'itchyny/lightline.vim'
	Plug 'jiangmiao/auto-pairs'
	Plug 'preservim/nerdcommenter'
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'tpope/vim-surround'
	Plug 'junegunn/fzf.vim'
call plug#end()

set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching brackets.
set ignorecase              " case insensitive matching
set hlsearch                " highlight search results
set tabstop=4               " number of columns occupied by a tab character
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
"set cc=80                   " set an 80 column border for good coding style
filetype plugin indent on   " allows auto-indenting depending on file type
syntax on                   " syntax highlighting

nmap <C-o> :NERDTreeToggle<CR>

let g:user_emmet_leader_key=','

" Use Ctrl-space to trigger completion
inoremap <silent><expr> <c-space> coc#refresh()

" Open file for edit use Ctrl+P hotkey, to search text in project use Alt+F
nnoremap <A-f> :Ag<CR>
nnoremap <C-p> :Files<CR>

" Configure Prettier
command! -nargs=0 Prettier :CocCommand prettier.formatFile

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
     \ pumvisible() ? "\<C-n>" :
     \ <SID>check_back_space() ? "\<TAB>" :
     \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction