from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD,DWORD, HANDLE,BOOL

# Function to display message box
MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

print(MessageBoxA)

#TEXT for Message Box A
lpCaption =  LPCSTR(b'World')
#lpText =  LPCSTR(b'Hello')
# Constants for MessageBox
MB_OKCANCEL = 0x00000001

#Show the message box
#MessageBoxA(None, lpText, lpCaption, MB_OKCANCEL)

# Function to retrieve the username
GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = BOOL

# Get the username
buffer_size = DWORD(10)
buffer =  create_string_buffer(buffer_size.value)

GetUserNameA(buffer, byref(buffer_size))
print(buffer.value)

# Call GetUserNameA
if GetUserNameA(buffer, byref(buffer_size)):
    username = buffer.value.decode('utf-8')  # Decode the byte buffer to a string
    lpText = LPCSTR(('hello user ' + username).encode('utf-8'))  # Encode the concatenated string to bytes and convert to LPCSTR
    MessageBoxA(None, lpText, lpCaption, MB_OKCANCEL)
else:
    print("Failed to retrieve username")
