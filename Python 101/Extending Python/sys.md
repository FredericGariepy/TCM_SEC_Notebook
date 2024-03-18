`Sys` is a module, a standard libary related to the python runtime environment.

Use `import sys` to get started. Notice there is no need to write `from`.

```python
import sys

print('version:'+sys.version)
print('executable bin:'+sys.executable)
print('Platform:'+sys.platform)

# sys can be used to interact with stdin,stdout,stderr

# using while loop & input()
usrinpt = input('input :')
while usrinpt != 'exit':
    print('>> {}'.format(usrinpt))
    usrinpt = input('input :')

# using sys
for line in sys.stdin:
    if line.strip() == 'exit':
        break
    sys.stdout.write('>> {}'.format(line))

# flush
for i in range(1,5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

import time
for i in range(0,51):
    time.sleep(0.001)

    sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, '.'*(50-i) ) )
    sys.stdout.flush()

# Note: \r character is a carriage return, allows you to overwrite current line with new content.

# sys to acces command line arg passed to script.
print("\n")
print(sys.argv)
# sys.argv[0] will always be the name of the script itself.

username = None
password = None
if len(sys.argv) != 3:
    sys.stdout.write("[X] To run {} enter username and password".format(sys.argv[0]))
    sys.stdout.flush()

# assing passed arguments to variables
elif len(sys.argv) == 3:
    username =  sys.argv[1]
    password =  sys.argv[2]
    print("username:{} password:{}".format(username, password))

# sys.path is a list of directory names where Python looks for modules
print(sys.path)


# list of 10 first python modules
for index, module in enumerate(sys.modules):
    print(f"{index+1} : {module}")
    # Stop after printing 10 modules
    if index == 9:
        break
# Equivalent  Bash script : pip list | grep -v "^Package" | cut -d" " -f1

# use exit codes to know exit condition
if username == None:
    sys.exit(5)
    print("I will never be printed")
else:
    sys.exit(0)
    print("Neither will I ever be printed too!")
# Bash: echo $? >> 0 || 5
```
