[The Python Package Index (PyPI) is a repository of software for the Python programming language.](https://pypi.org)

- Modules are libraries of code.
- `pip` is the python package manager to install modules.
-  Unless inside a venv, pip install are global. (Default: current wd dosen't matter)

In command line:  `pip install pwntools`

In .py file:  `from pwntools import *`

List all modules installed with pip: `pip list`

Install a specific verison: `pip install pwntools==4.5.1` | `pip install package_name==version`

List specific library versions: `pip freeze`

Uninstall :  `pip uninstall pwntools`

__requirements.txt__ is a file that lists modules required to run a script.

Install the requirements using the Requirements.txt file with `pip install -r requirements.txt`

You can generate a _requirements.txt_ file, IN __venv__ using `pip freeze > requirements.txt`
