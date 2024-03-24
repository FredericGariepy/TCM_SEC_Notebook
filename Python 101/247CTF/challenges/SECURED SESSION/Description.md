### SECURED SESSION
##### RATED MODERATE
If you can guess our random secret key, we will tell you the flag securely stored in your session.
___
### Solution
When hitting `https://1615f3b2ae1a7743.247ctf.com/` we see some python flask code:
```python
import os
from flask import Flask, request, session
from flag import flag

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def secret_key_to_int(s):
    try:
        secret_key = int(s)
    except ValueError:
        secret_key = 0
    return secret_key

@app.route("/flag")
def index():
    secret_key = secret_key_to_int(request.args['secret_key']) if 'secret_key' in request.args else None
    session['flag'] = flag
    if secret_key == app.config['SECRET_KEY']:
      return session['flag']
    else:
      return "Incorrect secret key!"

@app.route('/')
def source():
    return "
%s
" % open(__file__).read()

if __name__ == "__main__":
    app.run()
```
There's a few things happening here, but the most important is:
```python
session['flag'] = flag
```
This means that our flag is stored in our session.
<img src="https://github.com/FredericGariepy/TCM_SEC_Notebook/blob/main/Python%20101/247CTF/images/Screenshot%202024-03-24%20035418.jpg" alt="Finding session flag">

