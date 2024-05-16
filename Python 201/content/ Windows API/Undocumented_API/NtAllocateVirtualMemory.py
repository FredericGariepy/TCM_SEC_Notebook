'''
LETS TRANSLATE OUR PREVIOUS ALLOCATION SCRIPT, ONE LAYER DOWN.

So far the workflow has been :
Find a MSTN function def, make it in python, run the script.
Those API calls have been from User in Kernel 32, translated in low level by NTDLL..

However,
anti-virus, endpoint detection, responce solutions,
make use of API hooking to generate telemetry for their analysis

use low level API not hooked by security product.. 
API in NTDLL are mostly undocumented, can change at anytime with Windows releases

LETS TRANSLATE OUR PREVIOUS ALLOCATION SCRIPT, ONE LAYER DOWN.
https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntallocatevirtualmemory
https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess
'''

from ctypes import wintypes
from ctypes import windll
from ctypes import *

nt =  windll.ntdll
NTSTATUS = wintypes.DWORD

NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
NtAllocateVirtualMemory.restype = NTSTATUS

# retrieve a pseudo handle, special constant  0x 16*f
handle = 0xffffffffffffffff #https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess
base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 12)

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

ptr2 =  NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
  print("Error", hex(ptr2))

print("NtAllocateVirtualMemory: ", hex(base_address.value))

input() # this is just to hold the process 
