## Set {}
A set is an __unordered__ collection which does not support duplicate data.

#### Set constructor with, `{}` or  `set((val))`
`set_1 = {1,a,42j,True}`

or

`set_1 = set((1,2,3))`

#### length, `len(set)`
`len(set)` Gives you the number of objects contained in the set.
#### add to a set, `.add(val)`
`set.add(7)`
#### add _set_ or _list_ to a set, `.update(collection)`
`set.update(collection)` This will get rid of duplicate values.

`set.update(set_2)`  `set.update(list)`

Note: __False and 0, True and 1, will evaluate to the same data, hence in a set the last added will be autmatically removed.
#### union of sets, `.union(set_2)`
`set.union(set_2)`
#### `.union` VS `.update`
`.union` will combine both sets and return a copy of the union.

`.update` will change the set on which the operation takes place!
#### remove from set, `.remove(val)`
`set.remove(0)` Note: _if the value does not exist, a __KeyError__ will be thrown._
#### discard from set, `.discard(val)`
`set.discard(0)` Note: __No errors will be raised__
#### remove and return __random__ item from set, `pop()`
`set.pop()` Will return a _random_ item since Set is an _unordered_ collection.
