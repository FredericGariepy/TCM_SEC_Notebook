### VirtualAlloc:
This function is part of the Windows API and is commonly used by user-mode applications to allocate memory within their own address space.

### NtAllocateVirtualMemory:
Part of the Windows Native API (NT API) and is typically used for system-level programming or interacting with the Windows kernel.

### Use case

Malware attempting to hide its presence in memory can use process hollowing (unmapping legitimate code and replacing it with malicious code)
or process injection (injecting malicious code into a legitimate process).

#### functions can be used for malware memory allocation detection
API Hooking:
Hook memory allocation functions like `VirtualAlloc` but might overlook `NtAllocateVirtualMemory` calls.
