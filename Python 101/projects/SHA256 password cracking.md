Another stupid simple script, pwn Tools is not necessary here... log just make it look cool.

Were basically going though a list and encoding each word until it's hash corresponds to the hash we are looking for..

`python3 sha263crack.py e9236ffd48e1b70240a01d9a5216d7843ac02583fc5603fbafe3dabedb365640`

`[+] cracking e9236ffd48e1b70240a01d9a5216d7843ac02583fc5603fbafe3dabedb365640:`

`Atttemp:9997| Success! Password evangeli hashes to e9236ffd48e1b70240a01d9a5216d7843ac02583fc5603fbafe3dabedb365640`

Make a hash to test

```python
import sys
import hashlib

if len(sys.argv) != 2:
    print("{} takes 1 argument to produce <sha256sum>".format(sys>    sys.exit()

def sha256sum(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(sha256sum(sys.argv[1]))
```

Use the script to crack it.

```python
from pwn import *
import hashlib
import sys

#in sys param 1 is name of file
if len(sys.argv) != 2:
    print("{} takes 1 argument: <sha256sum>".format(sys.argv[0]))
    exit()
hashToCrack = sys.argv[1]
password_file = '10k-most-common.txt'
attempts = 0

def cleanpass(dirtypass):
    return dirtypass.strip('\n').encode('latin-1')

#made my own, my import of pwntools is giving me problems...
def sha256sum(data):
    return hashlib.sha256(data).hexdigest()

with log.progress("cracking {}".format(hashToCrack)) as p:
    with open(password_file, 'r', encoding='latin-1') as password_list:
        for password  in password_list:
            password = cleanpass(password)
            password_hash = sha256sum(password)
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'),password_hash))
            if password_hash == hashToCrack:
                p.success("Atttemp:{}| Success! Password {} hashes to {}".format(attempts,password.decode('latin-1'),hashToCrack))
                exit()
            attempts +=1
        p.failure('No password found')
```
