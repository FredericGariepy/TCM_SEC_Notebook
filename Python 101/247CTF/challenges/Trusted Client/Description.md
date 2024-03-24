### Trusted Client
##### Rated: Moderate

Developers don't always have time to setup a backend service when prototyping code.

Storing credentials on the client side should be fine as long as it's obfuscated right?
___
### Solution

I wrote a simple [python script](https://github.com/FredericGariepy/TCM_SEC_Notebook/blob/main/Python%20101/247CTF/challenges/Trusted%20Client/get_obfuscated_content.py) that parses the response for the contents of the first script tag.

The contents are written to a file. On inspecting the file, the built-in synntax hightlighter showed that the obfuscated content containted distinct blocks.

When passing the first two blocks into a javascript chrome terminal:

```javascript
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]
[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]

```
I got:
> ƒ Function() { [native code] }

This means that there is code implemented in the JavaScript engine itself, So I passed the remaining code blocks into the terminal and solved the Challenge:

<img src="https://github.com/FredericGariepy/TCM_SEC_Notebook/blob/main/Python%20101/247CTF/images/CTF%20TRUSTED%20CLIENT%202024_03_24.jpg" alt="Solution">
