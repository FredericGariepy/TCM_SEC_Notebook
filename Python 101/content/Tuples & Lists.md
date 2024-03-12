## Tuples ()
Tuples are immutable. They can be combined, but may not be changed.

Meaning: cannot append. `+` is possible however.

e.g. : `tupC = tupA + tupB`

### declaring tuples
`a = 0b1`

`tuple = ("1",1,a)`

__>>>__ ('1', 1, 1)

<class 'tuple'>

#### overloaded multiplication operator
`tuple_repeat = (0,) * 4`

__>>>__ (0, 0, 0, 0)

Note: _make sure to use `,` at the end of the closing `)`_

#### check if item exits `in` 
`1 in tuple` __>>>__ True
#### check index `.index()`
`tuple.index(1)` __>>>__ 1
#### index access `tuple[indx]`
`tuple[0]` __>>>__ '1'
#### access last item `[-1]`
`tuple[-1]` __>>>__ 1
`tuple[-3]` __>>__ '1'
#### slice with indexing [:]
`tuple[1:]` __>>>__ (1,1)
#### length of tuple `len()`
`len(tuple)` __>>>__ 3

## Lists []
Lists are mutable & ordered.
Just like arrays in Java, save that Lists in Python can take in any data type as its elements.

`list = [1, 0b1, '1', [2, 0b10, '2'] ]`

`2 in list1` __>>>__ False

`2 in list1[3]` __>>>__ True

`list[3][1]` __>>>__ 2

#### change, with index assignment
`list[0] = 3`
#### find index, `.index(val)`
`list.index(3)`
#### delete, `del` 
`del list[0]`
#### insert, `.insert(index,value)`
`list.inser(0,3)`
#### concatonate, with `+`
`new_list = [9]+list`  Adds 9 to start of list.
#### extend list, `.extend(other list)`
`list1.extend(list2)`
#### append, `.append(value)`
`list.append(7)`  Adds 7 to end of list.
#### Maximum, Minimum, `max()` `min()`
`max(list)` |  `min(list)`
#### reverse list, `.reverse()`
`list.reverse()`
#### reverse list, syntatic suggar `[::-1]`
`list[::-1]` _Note: [from: To: Step]_
#### Count value, `.count(val)`
`list.count(1)` __>>>__ int
#### Pop to remove and return last object from list, `.pop()`
`list.pop()`
#### clear the list, `.clear()`
`list.clear()` __>>>__ []
#### sort the list , `.sort()`
`list.sort()` Default sort: accending order

`list.sort(reverse=True)`  Return descending order
### Copy list data, `.copy()`
This method is important. 

`list1=[0]`

`list2=list1`

`list2.clear()`.

`list1` __>>>__ []

`list2` __>>>__ []

This is because list2 points to the address of list1.

It is not a new address.

To correctly manipulate list2, One should:

`list1=[0]`

`list2 =  list1.copy()`

`list2.clear()`

`list1` __>>>__ [0]

`list2` __>>__ []

### Apply function to all objects in the list, `list(map(function,list_name))` 
`list_1 = [2,4,6]`

`list(map(float, list_1))` __>>>__ [2.0, 4.0, 6.0]

With lambda (more on lambda in another chapter)

`list(map(lambda x: x % 2, list_1))` __>>>__ [0, 0, 0]
___
