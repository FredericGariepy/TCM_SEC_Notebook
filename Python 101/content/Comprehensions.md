## examples of comprehensiosn (list, sets, strings, nested expressions)
```
list = [1,2,3]

comprehension = [x for x in list]

conditional =  [x for x in list if x%2==0]

ranged = [x for x in range(1,4)]

functional = [hex(x) for x in ranged]

turnary_if_else = [bin(int(x, 16)) if int(x,16) > 0  else x for x in functional]

turnary_if_or = [i for i in range(13) if i ==0 or i%3==0]

nested_list = [[1,2,3],[7,8,9]]

nested_expression = [y for x in nested_list for y in x]
# >>> [1,2,3,7,8,9]

string = [s for s in "string"]

set = {x for x in range(5)}

joined = "".join(set)
# >>> 01234

deliniated_join = "-".join(set)
# >>> 0-1-2-3-4

```
