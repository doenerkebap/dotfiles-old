setlocal tabstop=2      " tab displays as 4 spaces
setlocal shiftwidth=2   " 2 spaces when indenting blocks in visual mode
setlocal softtabstop=2  " treat 2 spaces like a tab
setlocal expandtab      " insert spaces instead of tabs
setlocal smarttab       " use the shiftwidth setting instead of 'tabstop' when at the beginning of a line.

setlocal wrap           " Wrap lines at words
setlocal linebreak      " --
set spell
let &showbreak='   '    " chars to show before linebreak
let g:tex_comment_nospell=1 " Don't spell check comments

function! Synctex()
  " remove 'silent' for debugging
  execute "silent !zathura --synctex-forward " . line('.') . ":" . col('.') . ":" . bufname('%') . " " . g:syncpdf
  redraw!
endfunction


nnoremap <F6> :make current<CR>
nnoremap <F7> :make fig<CR>
nnoremap <F9> :make view<CR><C-c><CR>
nnoremap <F10> :call Synctex()<CR>
nnoremap <F11> :make view_fig<CR><C-c><CR>
