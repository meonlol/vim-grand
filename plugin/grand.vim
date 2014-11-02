if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif


" Get local path for the script, so we can import other files
let s:script_folder_path = escape( expand( '<sfile>:p:h' ), '\' )
let s:python_folder_path = s:script_folder_path . '/../python/'


command! GrandPaths call GrandPaths()
function! GrandPaths()
	execute "pyfile " . s:python_folder_path . "vim_grand_paths.py"
endfunction

command! GrandCtags call GrandCtags()
function! GrandCtags()
	execute "pyfile " . s:python_folder_path . "vim_grand_ctags.py"
endfunction


" We no longer need the stuff below. (right?)
function! AndroidGradleOld()
python << EOF
import vim

# The CWD is not searched for files by default. Add it
import os
import sys
#sys.path.append(os.getcwd())

script_path = vim.eval('s:python_folder_path')
lib_path = os.path.join(script_path, '.') 
print lib_path
sys.path.append(lib_path)

#print sys.path

from PathsResolver import PathsResolver


resolvedClassPaths = PathsResolver().getAllClassPaths()
resolvedSourcePaths = PathsResolver().getAllSourcePaths()
print resolvedClassPaths

vim.command("let $CLASSPATH = '" + ':'.join(resolvedClassPaths) + "'")
vim.command("let $SRCPATH = '" + ':'.join(resolvedSourcePaths) + "'")
vim.command("setlocal path=" + ','.join(resolvedClassPaths))

vim.command("silent! call javacomplete#SetClassPath($CLASSPATH)")
vim.command("silent! call javacomplete#SetSourcePath($SRCPATH)")

EOF
endfunction




function! AndroidUpdateTags()
python << EOF
import vim
import os
import sys
#sys.path.append(os.getcwd())

script_path = vim.eval('s:python_folder_path')
lib_path = os.path.join(script_path, '.') 
print lib_path
sys.path.append(lib_path)

from TagsHandler import TagsHandler

TagsHandler().generateTagsFile()


EOF
endfunction




