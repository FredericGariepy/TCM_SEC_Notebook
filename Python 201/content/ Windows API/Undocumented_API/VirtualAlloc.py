'''
Not all Window APIs are document on MSDN
When calling user mode API we will end up in kernel mode 
Windpws API are abstraction layers on top of Native API
Native API calls are defined in NTDLL
Well documented User mode APIs are dpocumented in NTDLL
https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc
'''

from ctypes import wintypes
from ctypes import windll
from ctypes import *

kernel32 = windll.kernel32

SIZE_T =  c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = [wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD]
VirtualAlloc.restype = wintypes.LPVOID #LPVOID pointer to void object

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

ptr =  VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE) #Print the memory allocated

error = GetLastError()
if error:
  print(error)
  print(WinError(error))

print("VirtualAlloc: ", hex(ptr))

input() # this is just to hold the process
