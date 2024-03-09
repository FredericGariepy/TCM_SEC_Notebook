# Vim (full feature editor)
**Essentials:** by default we enter Command mode.

##  Exit Vim  `:q` `:q!` `:wq`
`esc` to exit input or lastline mode.

`:q` to exit vim.

`:q!: to exit without saving changes.

`:wq: to save changes, and exit.

### search `/`

### moving around `h` `j` `k` `l`
**Some command lines might not have arrow keys enabled (remote shells)**
|`key` | movement |
|-|-|
|`h` |left |
|`j` |down |
|`k` |up |
|`l` |right |

### Insert mode `i` , then `esc` to return into command mode
### Delete `x` (in command mode)
### Undo `u` (in command mode)
### Redoo `ctrl`**+**`R` (in command mode)
### `dd` Delete line
`2 dd` delete two lines. Change number to number of lines to delete.

## Copy/paste|cut (In Visual mode `v`)
Start Copy `v`. This enters visual mode and starts selection.

Note: the char highlighted and __*right of cursor* are also selected__.

End copy `y`. This ends viusal mode. 
Cut with `c`. This enters Insert mode.

Paste with `p`. 
