## Taking-in user input
Interact with running user input.

Input is flow breaking and will wait for input before continuing.

### User input, `input()`
```
usrName = input("say hello to user: ")
print("Hello {}".format(usrName))

Print("Enter IP to exploit. Enter exit to quit")
while True:
    ip =  input("Enter IP: ")
    if ip == "exit":
        break
    else:
        print(f"exploiting {ip}")
```
