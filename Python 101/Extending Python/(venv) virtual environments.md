## `pip install virtualenv`
Virtual enviroments enables isolated python environment. NOT dependent on host system or virual env packgages.

Multiple venv can run _at the same time_ with diffrent modules or versions.
#### Start venv, `python3 -m venv env`
#### Use venv, `source end/bin/activate`
`(end)user@host~`

__No__ packages will be installed on this venv.

The binary from which python is executed differs.
| environment | command | output |
|-|-|-|
|host|`which python3` | /usr/bin/python3|
|venv|`which python3`| /home/user/directory/.../__env/bin/python3__ |
### finish with your venv `deactivate`
