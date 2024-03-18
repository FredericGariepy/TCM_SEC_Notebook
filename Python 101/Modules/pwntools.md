<img src="https://pypi-camo.freetls.fastly.net/16d82a21c9635a10273ddd2595958d6c66216963/68747470733a2f2f6769746875622e636f6d2f47616c6c6f70736c65642f70776e746f6f6c732f626c6f622f737461626c652f646f63732f736f757263652f6c6f676f2e706e673f7261773d74727565" alt="PWN" width="200">
A very powerfull python module for hacking.

## Set-up
### GET [GNU Binutils](https://www.gnu.org/software/binutils/)
Get it here: `git clone git://sourceware.org/git/binutils-gdb.git`

I'm working in Windows. So, I run my Linux inside a Windows Subsystem for Linux [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

Install pwntools: `pip install pwntools`

Because I'm in WSL, I need to __add /bin directory to system's PATH__ environment variable.

In my case: `export PATH="$PATH:/home/fred/.local/bin"`

> All executables installed in .local/bin (such as pwntools) can be run anywehere in terminal without specifying their full path.
> Okay, let's get cracking!

```python
# exploits.py
from pwn import *
print(cyclic(50))
print(cyclic_find('laaa'))

print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))
```
___

``` bash
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama'
44
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push b'/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, esp
    xor edx, edx
    /* call execve() */
    push SYS_execve /* 0xb */
    pop eax
    int 0x80

00000000  6a 68 68 2f  2f 2f 73 68  2f 62 69 6e  89 e3 68 01  │jhh/│//sh│/bin│··h·│
00000010  01 01 01 81  34 24 72 69  01 01 31 c9  51 6a 04 59  │····│4$ri│··1·│Qj·Y│
00000020  01 e1 51 89  e1 31 d2 6a  0b 58 cd 80               │··Q·│·1·j│·X··│
0000002c
```
